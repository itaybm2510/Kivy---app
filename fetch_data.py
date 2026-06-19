import ccxt
import pandas as pd
import time

def fetch_massive_futures_data(symbol='BTC/USDT', timeframe='1h', total_candles=10000):
    print(f"🔄 Connecting to Bybit... Fetching {total_candles} candles for {symbol}...")
    exchange = ccxt.bybit({'enableRateLimit': True, 'options': {'defaultType': 'linear'}})
    
    all_candles = []
    # נקודת התחלה - עכשיו
    since = None 
    
    while len(all_candles) < total_candles:
        try:
            # משיכת חופנים של 1000 נרות בכל פעם
            candles = exchange.fetch_ohlcv(symbol, timeframe, since=since, limit=1000)
            if not candles:
                break
                
            all_candles.extend(candles)
            # עדכון הזמן לנר הכי ישן שקיבלנו כדי להמשיך אחורה בזמן
            since = candles[0][0] - (1000 * 60 * 60 * 1000) 
            print(f"📥 Collected {len(all_candles)}/{total_candles} candles...")
            time.sleep(0.2) # הגנה מחסימה של הבורסה
        except Exception as e:
            print(f"⚠️ Error fetching chunk: {e}")
            time.sleep(2)
            
    # סידור הדאטה כרונולוגית מהישן לחדש
    all_candles = sorted(all_candles, key=lambda x: x[0])
    all_candles = all_candles[-total_candles:] # לקיחת הכמות המדויקת שביקשנו
    
    columns = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
    df = pd.DataFrame(all_candles, columns=columns)
    df['Timestamp'] = pd.to_datetime(df['Timestamp'], unit='ms')
    
    df.to_csv('btc_futures_data.csv', index=False)
    print("💾 Massive dataset saved successfully to 'btc_futures_data.csv'!")

if __name__ == "__main__":
    fetch_massive_futures_data()

