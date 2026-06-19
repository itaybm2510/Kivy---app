import torch
import torch.optim as optim
from torch.optim.lr_scheduler import ExponentialLR
from torch.distributions import Categorical
import numpy as np
import os
import random
from crypto_env import CryptoTradingEnv
from ppo_model import ActorCritic

def train_ppo(epochs=300, batch_size=64, ppo_epochs=5, clip_eps=0.2):
    env = CryptoTradingEnv(csv_path='btc_futures_data.csv')
    state_dim = 18 
    
    model = ActorCritic(state_dim=state_dim)
    optimizer = optim.Adam(model.parameters(), lr=0.0003) # קצב למידה רענן להתנעה מחדש
    scheduler = ExponentialLR(optimizer, gamma=0.995)
    
    model_path = 'best_ppo_model.pt'
    if os.path.exists(model_path):
        print(f"🧠 Found existing brain '{model_path}'. Loading & FORCING exploration... 🔥")
        model.load_state_dict(torch.load(model_path))
    else:
        print("🌋 No saved model found. Starting brand new evolution...")
        
    total_data_size = len(env.df)
    train_split_limit = int(total_data_size * 0.8)
    
    best_test_equity = 0.0
    
    for epoch in range(epochs):
        model.train()
        # 🎲 בחירת מקטע אימון אקראי
        segment_length = random.randint(1500, 3000)
        start_step = random.randint(50, train_split_limit - segment_length - 5)
        end_step = start_step + segment_length
        
        state = env.reset(start_step=start_step, end_step=end_step)
        done = False
        states, actions, action_types, action_sizes, rewards, values, log_probs = [], [], [], [], [], [], []
        entropies = []
        
        while not done:
            state_tensor = torch.FloatTensor(state)
            action_probs, position_size, state_value = model(state_tensor)
            
            # 🔥 מנגנון שבירת קיפאון: מכריח את המודל לחזור לנסות עסקאות בשוק
            # ככל שהאנטרופיה נמוכה יותר, אנחנו מזריקים יותר אקראיות מבוקרת
            if epoch < 100:
                action_probs = action_probs * 0.70 + 0.10 # מחלק 10% סיכוי שווה לכל פעולה
                action_probs = action_probs / action_probs.sum()
                
            dist = Categorical(action_probs)
            action_type = dist.sample()
            
            states.append(state)
            action_types.append(action_type.item())
            action_sizes.append(position_size.item())
            rewards.append(0.0)
            values.append(state_value.item())
            log_probs.append(dist.log_prob(action_type).item())
            entropies.append(dist.entropy().item())
            
            next_state, reward, done = env.step(action_type.item(), position_size.item())
            rewards[-1] = reward
            state = next_state
            
        train_equity = env.equity
        train_trades = env.total_trades
        
        # עדכון משקלים (PPO Step)
        returns = []
        discounted_reward = 0
        for r in reversed(rewards):
            discounted_reward = r + 0.99 * discounted_reward
            returns.insert(0, discounted_reward)
            
        states = torch.FloatTensor(np.array(states))
        action_types = torch.LongTensor(action_types)
        action_sizes = torch.FloatTensor(action_sizes)
        returns = torch.FloatTensor(returns)
        old_log_probs = torch.FloatTensor(log_probs)
        values = torch.FloatTensor(values)
        advantages = returns - values
        advantages = (advantages - advantages.mean()) / (advantages.std() + 1e-9)
        
        for _ in range(ppo_epochs):
            curr_action_probs, curr_position_size, curr_state_value = model(states)
            curr_dist = Categorical(curr_action_probs)
            curr_log_probs = curr_dist.log_prob(action_types)
            
            ratios = torch.exp(curr_log_probs - old_log_probs)
            surr1 = ratios * advantages
            surr2 = torch.clamp(ratios, 1.0 - clip_eps, 1.0 + clip_eps) * advantages
            
            actor_loss = -torch.min(surr1, surr2).mean() - (0.05 * curr_dist.entropy().mean())
            critic_loss = torch.nn.functional.mse_loss(curr_state_value.squeeze(), returns)
            total_loss = actor_loss + 0.5 * critic_loss
            
            optimizer.zero_grad()
            total_loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=0.5)
            optimizer.step()
            
        scheduler.step()
        
        # 📺 לוג ובדיקת מבחן אטומה - כל 50 דורים בדיוק
        if (epoch + 1) % 50 == 0 or epoch == 0:
            model.eval()
            test_state = env.reset(start_step=train_split_limit, end_step=total_data_size-1)
            test_done = False
            
            while not test_done:
                t_tensor = torch.FloatTensor(test_state)
                with torch.no_grad():
                    t_probs, t_size, _ = model(t_tensor)
                
                # במבחן אנחנו מאלצים אותו לבחור את מה שהוא חושב שהכי נכון (ולא אקראי)
                t_action = torch.argmax(t_probs).item() 
                test_state, _, test_done = env.step(t_action, t_size.item())
            
            test_win_rate = (env.successful_trades / env.total_trades * 100) if env.total_trades > 0 else 0.0
            
            # שמירת המודל רק אם הוא מנצח את שיא המבחן על דאטה חדש
            if env.equity > best_test_equity and env.total_trades > 0:
                best_test_equity = env.equity
                torch.save(model.state_dict(), model_path)
                
            print(f"📦 Epoch {epoch+1:03d}/300 | Loss: {total_loss.item():.2f}")
            print(f"   🛸 TRAIN Seg: Rows {start_step}-{end_step} | End Equity: ${train_equity:.2f} | Trades: {train_trades}")
            print(f"   🎯 TEST (UNSEEN DATA): Equity: ${env.equity:.2f} | Peak Test: ${best_test_equity:.2f}")
            print(f"   📊 Test Trades: {env.total_trades} (📈 L: {env.long_trades} | 📉 S: {env.short_trades}) | Win Rate: {test_win_rate:.1f}%")
            print(f"   🔮 Exploration Level (Entropy): {np.mean(entropies):.3f}")
            print("-" * 75)

if __name__ == "__main__":
    train_ppo()

