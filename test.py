import urllib.request
import urllib.parse

ADMIN_BOT_TOKEN = '8798801569:AAE1IRyI4P5q9TVbN7h-x7NhtnxviGvEqQw'
ADMIN_ID = 2001911239
text = "🚀 בדיקה: אם אתה רואה את ההודעה הזו, החיבור לבוט השני תקין לחלוטין!"

try:
    url = f"https://api.telegram.org/bot{ADMIN_BOT_TOKEN}/sendMessage?chat_id={ADMIN_ID}&text={urllib.parse.quote(text)}"
    urllib.request.urlopen(url, timeout=5)
    print("✅ ההודעה נשלחה בהצלחה! תבדוק את הבוט השני בטלגרם.")
except Exception as e:
    print(f"❌ שגיאה בשליחה: {e}")
    print("משמעות השגיאה: או שלא לחצת /start בבוט השני, או שהטוקן/ID לא מדויקים.")

