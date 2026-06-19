import json
import logging
import ccxt
import pandas as pd
import ta
import os
import sys
import time
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

print("[1/4] מאתחל טרמינל מסחר אמיתי מבוסס Binance...")
sys.stdout.flush()

# הטוקן הנקי ללא הקו התחתון בסוף
TELEGRAM_TOKEN = "8132400945:AAHzQ6vlrYutGQApJby-eQbqPVj5WsOdCFE"
USER_CHAT_ID = "2001911239"
DATA_FILE = "bot_data.json"

SCAN_SYMBOLS = ["BTC/USDT", "ETH/USDT", "SOL/USDT", "XRP/USDT"]
LEVERAGE = 3             
RISK_PER_TRADE = 0.05    

is_scanning_active = False
trades_history = []
account_balance = 10000.0  

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def load_data():
    global trades_history, account_balance
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                saved_data = json.load(f)
                if isinstance(saved_data, dict):
                    trades_history = saved_data.get("history", [])
                    account_balance = saved_data.get("balance", 10000.0)
            print(f"[*] בסיס הנתונים סונכרן. יתרה: ${account_balance:,.2f}")
        except Exception as e:
            print(f"[-] שגיאה בטעינת קובץ זיכרון: {e}")
    sys.stdout.flush()

def save_data():
    global trades_history, account_balance
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump({"history": trades_history, "balance": account_balance}, f, indent=4)
    except Exception as e:
        print(f"[-] שגיאה בשמירת קובץ הזיכרון: {e}")

def get_public_exchange():
    return ccxt.binance({'enableRateLimit': True, 'options': {'defaultType': 'future'}})

def analyze_market_advanced(exchange, symbol):
    try:
        bars_5m = exchange.fetch_ohlcv(symbol, timeframe="5m", limit=30)
        df_5m = pd.DataFrame(bars_5m, columns=['t', 'o', 'h', 'l', 'close', 'v'])
        ema9_5m = ta.trend.ema_indicator(df_5m['close'], window=9).iloc[-2]
        ema21_5m = ta.trend.ema_indicator(df_5m['close'], window=21).iloc[-2]
        macro_trend = "BULLISH" if ema9_5m > ema21_5m else "BEARISH"

        bars_1m = exchange.fetch_ohlcv(symbol, timeframe="1m", limit=30)
        df_1m = pd.DataFrame(bars_1m, columns=['t', 'o', 'h', 'l', 'close', 'v'])
        
        rsi = ta.momentum.rsi(df_1m['close'], window=14).iloc[-2]
        ema9_1m = ta.trend.ema_indicator(df_1m['close'], window=9).iloc[-2]
        ema21_1m = ta.trend.ema_indicator(df_1m['close'], window=21).iloc[-2]
        price = df_1m['close'].iloc[-1]
        
        # אסטרטגיה רגישה ומהירה כדי לקבל אינדיקציה מיידית בשוק חי
        if macro_trend == "BULLISH" and ema9_1m > ema21_1m and rsi > 45:
            return {"d": "BUY_LONG", "p": price, "reason": "פריצת מומנטום חיובית בשוק חי"}
        if macro_trend == "BEARISH" and ema9_1m < ema21_1m and rsi < 55:
            return {"d": "SELL_SHORT", "p": price, "reason": "שבירת מומנטום שלילית בשוק חי"}
            
        return {"d": "HOLD", "p": price, "info": f"RSI: {rsi:.1f}"}
    except Exception as e:
        return {"d": "ERROR", "err": str(e)}

async def scan_market_job(context: ContextTypes.DEFAULT_TYPE):
    global trades_history, is_scanning_active, account_balance
    if not is_scanning_active: return

    print(f"\n[💓 HEARTBEAT] {time.strftime('%H:%M:%S')} - סורק שוק אמיתי (Binance)...")
    sys.stdout.flush()

    try:
        exchange = get_public_exchange()
    except Exception as e:
        print(f"  ⚠️ כשל בחיבור ראשוני לבורסה: {e}")
        return

    for symbol in SCAN_SYMBOLS:
        if any(t['status'] == 'OPEN' and t['symbol'] == symbol for t in trades_history):
            continue

        data = analyze_market_advanced(exchange, symbol)
        
        if data.get("d") == "HOLD":
            print(f"  ↳ 🔍 {symbol}: מחיר נוכחי ${data['p']:,.2f} | {data['info']} -> ממתין לאיתות")
            sys.stdout.flush()
            continue
        elif data.get("d") == "ERROR":
            print(f"  ↳ ❌ {symbol}: שגיאת רשת! פירוט: {data.get('err')}")
            sys.stdout.flush()
            continue

        if data['d'] in ['BUY_LONG', 'SELL_SHORT']:
            price = data['p']
            decision = data['d']
            
            trade_margin = account_balance * RISK_PER_TRADE
            position_size_usd = trade_margin * LEVERAGE
            
            new_trade = {
                "symbol": symbol, "type": decision, "entry": price, "status": "OPEN",
                "sl": price * 0.99 if decision == "BUY_LONG" else price * 1.01,
                "tp": price * 1.02 if decision == "BUY_LONG" else price * 0.98,
                "margin": trade_margin, "position_size": position_size_usd,
                "reason": data['reason']
            }
            trades_history.append(new_trade)
            save_data()
            
            entry_card = f"""
⚡ **עסקה אמיתית נפתחה בשוק!**
◤===================================◥
  🪙 **נכס:** `{symbol}`
  🧭 **כיוון פוזיציה:** `{decision}`
  🎯 **שער כניסה:** `${price:,.4f}`
  🔬 **סיבה טכנית:** `{data['reason']}`
◣===================================◢
            """
            print(f"  ↳ 🚀 {symbol}: האיתות נתפס ונשלח לטלגרם!")
            sys.stdout.flush()
            await context.bot.send_message(chat_id=USER_CHAT_ID, text=entry_card, parse_mode="Markdown")
            break 

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [['⚡ הפעל טרמינל מסחר']]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("🖥️ **המערכת חוברה בהצלחה לטלגרם**\nלחץ על הכפתור כדי להתחיל סריקה חיה:", reply_markup=reply_markup)

async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global is_scanning_active
    text = update.message.text
    if text == '⚡ הפעל טרמינל מסחר':
        is_scanning_active = True
        await update.message.reply_text("🚀 המנוע עלה לאוויר! סורק בבינאנס בכל 30 שניות...")
        context.job_queue.run_repeating(scan_market_job, interval=30, first=1, name="trading_job", job_kwargs={'misfire_grace_time': 15})

if __name__ == '__main__':
    load_data()
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_messages))
    print("=== [המערכת מאותחלת ומחכה להפעלה בטלגרם] ===")
    sys.stdout.flush()
    app.run_polling()

