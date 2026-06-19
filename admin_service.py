import asyncio
from flask import Flask, request, jsonify
from telegram import Bot

app = Flask(__name__)

ADMIN_BOT_TOKEN = '8982961757:AAHVqGjuWxKRTouAVlrEI4Oaz9uqiwMVWNs'
ADMIN_ID = 2001911239

# פונקציה אסינכרונית לשליחת ההודעה לטלגרם
async def send_to_telegram(text):
    bot = Bot(token=ADMIN_BOT_TOKEN)
    async with bot:
        await bot.send_message(chat_id=ADMIN_ID, text=text, parse_mode='Markdown')

@app.route('/send_order', methods=['POST'])
def handle_order():
    data = request.json
    if not data or 'text' not in data:
        return jsonify({"status": "error", "message": "No text provided"}), 400
    
    order_text = data['text']
    
    # הרצת השליחה האסינכרונית בתוך השרת הסינכרוני של פלאסק
    try:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(send_to_telegram(order_text))
        loop.close()
        return jsonify({"status": "success"}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    print("🛰️ שרת ניהול ההזמנות באוויר ומקשיב על פורט 5000...")
    app.run(host='127.0.0.1', port=5000, debug=False)

