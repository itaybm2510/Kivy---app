import torch
from torch.distributions import Categorical
import numpy as np
import pandas as pd
from crypto_env import CryptoTradingEnv
from ppo_model import ActorCritic

def run_backtest():
    csv_path = 'btc_futures_data.csv'
    model_path = 'best_ppo_model.pt'
    
    # 1. טעינת הסביבה
    env = CryptoTradingEnv(csv_path=csv_path)
    
    # 2. חותכים את הסביבה כך שהבדיקה תרוץ רק על ה-30% האחרונים של הקובץ (תוכן חדש עבורו)
    total_rows = len(env.df)
    test_start_step = int(total_rows * 0.7) 
    print(f"🎬 Starting Backtest on UNSEEN data (Last 30% of CSV: Rows {test_start_step} to {total_rows})...")
    
    # 3. טעינת המוח המנצח
    state_dim = 18
    model = ActorCritic(state_dim=state_dim)
    
    try:
        model.load_state_dict(torch.load(model_path))
        model.eval() # מעביר את המודל למצב בדיקה (מכבה את הלימוד והרעש)
        print(f"🧠 Successfully loaded the best brain from '{model_path}'!")
    except:
        print(f"❌ Error: Could not find or load '{model_path}'. Make sure it exists.")
        return

    # 4. הרצת הסימולציה
    state = env.reset()
    env.current_step = test_start_step # מקפיצים את הבוט ישירות לחלק של המבחן
    
    done = False
    history_equity = []
    
    print("\n🚀 Simulation is running...")
    
    while not done:
        state_tensor = torch.FloatTensor(state)
        with torch.no_grad(): # אין צורך בחישוב גרדיאנטים בבדיקה
            action_probs, position_size, _ = model(state_tensor)
        
        # במצב בדיקה אמיתי, אנחנו לא לוקחים מדגם אקראי (sample), אלא לוקחים את הפעולה עם ההסתברות הכי גבוהה (Argmax)
        action_type = torch.argmax(action_probs).item()
        
        next_state, reward, done = env.step(action_type, position_size.item())
        state = next_state
        history_equity.append(env.equity)

    # 📊 הדפסת דוח ביצועים של המבחן
    win_rate = (env.successful_trades / env.total_trades * 100) if env.total_trades > 0 else 0.0
    print("\n" + "="*50)
    print("📈 FINAL BACKTEST PERFORMANCE REPORT 📈")
    print("="*50)
    print(f"💰 Starting Balance:  $1000.00")
    print(f"💵 Ending Equity:      ${env.equity:.2f}")
    print(f"📊 Total Trades Done:  {env.total_trades} (📈 Long: {env.long_trades} | 📉 Short: {env.short_trades})")
    print(f"🎯 Test Win Rate:      {win_rate:.1f}%")
    print(f"💸 Total Fees Paid:    ${env.total_fees:.2f}")
    print(f"🛡️ Risk Control Hits: [🛑 Stop-Loss: {env.sl_hits} | 🟢 Take-Profit: {env.tp_hits}]")
    
    profit_loss_pct = ((env.equity - 1000.0) / 1000.0) * 100
    if env.equity > 1000:
        print(f"🟩 Result: SUCCESS! The model made a net profit of {profit_loss_pct:.1f}% on new data! 🔥")
    else:
        print(f"🟥 Result: OVERFITTING! The model lost {abs(profit_loss_pct):.1f}% on new data. Needs more data variety.")
    print("="*50)

if __name__ == "__main__":
    run_backtest()

