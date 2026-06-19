import numpy as np
import pandas as pd

class CryptoTradingEnv:
    def __init__(self, csv_path, initial_balance=1000.0, leverage=10, fee=0.0006, stop_loss_pct=0.015, take_profit_pct=0.045):
        self.df = pd.read_csv(csv_path)
        self.initial_balance = initial_balance
        self.leverage = leverage
        self.fee = fee 
        self.stop_loss_pct = stop_loss_pct     
        self.take_profit_pct = take_profit_pct 
        self.max_holding_hours = 48              
        
        self._add_advanced_indicators()
        self.reset()

    def _add_advanced_indicators(self):
        delta = self.df['Close'].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        rs = gain / (loss + 1e-9)
        self.df['RSI'] = (100 - (100 / (1 + rs))).fillna(50) / 100.0
        
        self.df['SMA_9'] = (self.df['Close'].rolling(window=9).mean() / self.df['Close']).fillna(1.0)
        self.df['SMA_25'] = (self.df['Close'].rolling(window=25).mean() / self.df['Close']).fillna(1.0)
        self.df['Spread'] = ((self.df['High'] - self.df['Low']) / self.df['Close']).fillna(0.0)
        self.df['Norm_Volume'] = (self.df['Volume'] / self.df['Volume'].rolling(window=20).mean()).fillna(1.0)
        
        exp1 = self.df['Close'].ewm(span=12, adjust=False).mean()
        exp2 = self.df['Close'].ewm(span=26, adjust=False).mean()
        macd = exp1 - exp2
        signal = macd.ewm(span=9, adjust=False).mean()
        self.df['MACD_Hist'] = ((macd - signal) / self.df['Close']).fillna(0.0)

    def reset(self, start_step=50, end_step=None):
        self.balance = self.initial_balance
        self.equity = self.initial_balance
        self.current_step = start_step
        self.end_step = end_step if end_step is not None else len(self.df) - 1
        
        self.position = 0       
        self.entry_price = 0.0
        self.position_size = 0.0 
        self.trade_duration = 0 
        
        self.total_trades = 0
        self.long_trades = 0
        self.short_trades = 0
        self.total_fees = 0.0
        self.successful_trades = 0 
        self.sl_hits = 0           
        self.tp_hits = 0           
        
        return self._get_observation()

    def _get_observation(self):
        lookback = 10
        prices = self.df['Close'].iloc[self.current_step - lookback : self.current_step].values
        current_price = self.df['Close'].iloc[self.current_step]
        normalized_prices = prices / current_price
        
        rsi = self.df['RSI'].iloc[self.current_step]
        sma9 = self.df['SMA_9'].iloc[self.current_step]
        sma25 = self.df['SMA_25'].iloc[self.current_step]
        spread = self.df['Spread'].iloc[self.current_step]
        vol = self.df['Norm_Volume'].iloc[self.current_step]
        macd = self.df['MACD_Hist'].iloc[self.current_step]
        
        state = np.append(normalized_prices, [rsi, sma9, sma25, spread, vol, macd, self.position, self.balance / self.initial_balance])
        return state.astype(np.float32)

    def step(self, action_type, action_size):
        current_price = self.df['Close'].iloc[self.current_step]
        reward = 0.0
        done = False
        old_equity = self.equity
        action_penalty = 0.0
        
        if self.position != 0:
            self.trade_duration += 1
            price_change = (current_price - self.entry_price) / self.entry_price
            current_pnl_pct = price_change * self.position
            
            if current_pnl_pct <= -self.stop_loss_pct:
                action_type = 0 
                action_penalty = -0.5
                self.sl_hits += 1
            elif current_pnl_pct >= self.take_profit_pct:
                action_type = 0 
                action_penalty = 1.0 
                self.tp_hits += 1
            elif self.trade_duration >= self.max_holding_hours:
                action_type = 0
                action_penalty = -0.1

        if action_type == 0 and self.position != 0:
            pnl = self._calculate_pnl(current_price)
            fee_cost = self.position_size * self.fee
            net_pnl = pnl - fee_cost
            if net_pnl > 0: self.successful_trades += 1
            self.balance += net_pnl
            self.total_fees += fee_cost
            self.position = 0
            self.position_size = 0
            self.trade_duration = 0
            action_penalty += -0.02
            
        elif action_type == 1 and self.position != 1:
            if self.position == -1: 
                self.balance += self._calculate_pnl(current_price) - (self.position_size * self.fee)
            self.position = 1
            self.entry_price = current_price
            self.position_size = self.balance * max(0.1, action_size) * self.leverage
            fee_cost = self.position_size * self.fee
            self.balance -= fee_cost
            self.total_fees += fee_cost
            self.total_trades += 1
            self.long_trades += 1
            self.trade_duration = 0
            action_penalty += -0.08 # ⚖️ ריכוך קנס למניעת קיפאון
            
        elif action_type == 2 and self.position != -1:
            if self.position == 1: 
                self.balance += self._calculate_pnl(current_price) - (self.position_size * self.fee)
            self.position = -1
            self.entry_price = current_price
            self.position_size = self.balance * max(0.1, action_size) * self.leverage
            fee_cost = self.position_size * self.fee
            self.balance -= fee_cost
            self.total_fees += fee_cost
            self.total_trades += 1
            self.short_trades += 1
            self.trade_duration = 0
            action_penalty += -0.08 # ⚖️ ריכוך קנס למניעת קיפאון

        self.current_step += 1
        if self.current_step >= self.end_step or self.balance <= 10.0:
            done = True 

        next_price = self.df['Close'].iloc[self.current_step]
        self.equity = self.balance + self._calculate_pnl(next_price)
        
        balance_penalty = 0.0
        if self.total_trades > 5:
            long_ratio = self.long_trades / self.total_trades
            if long_ratio > 0.80 or long_ratio < 0.20:
                balance_penalty = -0.1 
        
        step_pnl = (self.equity - old_equity) / self.initial_balance
        reward = (step_pnl * 30.0) + action_penalty + balance_penalty
        
        return self._get_observation(), reward, done

    def _calculate_pnl(self, current_price):
        if self.position == 0: return 0.0
        change = (current_price - self.entry_price) / self.entry_price
        return self.position_size * change * self.position

