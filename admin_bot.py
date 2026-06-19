import sys
import asyncio
from telegram import Bot

ADMIN_BOT_TOKEN = '8982961757:AAHVqGjuWxKRTouAVlrEI4Oaz9uqiwMVWNs'
ADMIN_ID = 2001911239

async def send_order():
    if len(sys.argv) < 2:
        return
    
    # קבלת טקסט ההזמנה מהארגומנטים של מערכת ההפעלה
    message_text = sys.argv[1]
    
    try:
        bot = Bot(token=ADMIN_BOT_TOKEN)
        async with bot:
            await bot.send_message(chat_id=ADMIN_ID, text=message_text, parse_mode='Markdown')
        print("SUCCESS")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == '__main__':
    asyncio.run(send_order())

