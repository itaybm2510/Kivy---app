from flask import Flask
import os
from database import init_db
from templates_base import BASE_TEMPLATE
from routes import register_routes

# אתחול שרת ה-Flask של חברת הענק
app = Flask(__name__)

# מפתח אבטחה חזק להצפנת סל הקניות והקופונים ב-Session
app.secret_key = os.urandom(24)

# הפעלת מנגנון אתחול מסד הנתונים הארגוני (אם הקובץ לא קיים, הוא ייצר אותו)
init_db()

# רישום וחיבור כל הנתבים, דפי ה-Bento Grid ומנוע ה-AI
register_routes(app, BASE_TEMPLATE)

if __name__ == '__main__':
    print("=" * 60)
    print("🚀 SMARTBIZ MEGA-OS v5.0 IS INITIALIZING...")
    print("🔗 DATABASE CONNECTIONS: ONLINE")
    print("🤖 CONTEXT-AWARE AI ENGINE: ACTIVE & LISTENING")
    print("🌍 SERVER RUNNING ON: http://127.0.0.1:5000")
    print("=" * 60)
    
    # הרצת השרת במצב פיתוח (Debug Mode) כדי שכל שינוי יתעדכן מיד
    app.run(host='127.0.5.1', port=5004, debug=True)

