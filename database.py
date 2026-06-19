import sqlite3

DB_NAME = 'business_premium_v5.db'

def get_db_connection():
    """מייצר חיבור למסד הנתונים ומחזיר אותו במבנה של מילון נוח לגישה"""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """מאתחל את כל הטבלאות המורחבות של האתר"""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. טבלת מלאי מוצרים מורחבת (כולל תיאור וקטגוריה לטובת ה-AI)
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        name TEXT NOT NULL, 
                        price REAL NOT NULL, 
                        stock INTEGER NOT NULL,
                        category TEXT DEFAULT 'כללי',
                        description TEXT DEFAULT '')''')
    
    # 2. טבלת הזמנות CRM (כולל תיעוד הנחות מורחב)
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        items TEXT NOT NULL, 
                        total REAL NOT NULL, 
                        phone TEXT NOT NULL, 
                        address TEXT NOT NULL, 
                        status TEXT DEFAULT '⏳ בהמתנה', 
                        coupon_used TEXT DEFAULT NULL, 
                        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # 3. טבלת קופונים
    cursor.execute('''CREATE TABLE IF NOT EXISTS coupons (
                        code TEXT PRIMARY KEY, 
                        discount_percent INTEGER NOT NULL)''')
    
    # 4. טבלת הוצאות עסק
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        amount REAL NOT NULL, 
                        description TEXT NOT NULL, 
                        date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    
    # 5. טבלת משתמשי מערכת והרשאות (עבור מנהלים / עובדים / שליחים)
    cursor.execute('''CREATE TABLE IF NOT EXISTS staff (
                        username TEXT PRIMARY KEY,
                        pin TEXT NOT NULL,
                        role TEXT NOT NULL)''') # Roles: 'admin', 'staff', 'delivery'
    
    # הכנסת מוצרי דוגמה עשירים (עם קטגוריות ותיאורים עבור ה-AI והחיפוש)
    if cursor.execute("SELECT COUNT(*) FROM inventory").fetchone()[0] == 0:
        sample_products = [
            ("💻 CyberBook Pro 16 X", 5400, 12, "מחשבים", "מחשב על לגיימינג ותכנות, מעבד קוונטי מואץ, 32GB RAM"),
            ("🎧 Quantum Sound ANC Neo", 950, 30, "סאונד", "אוזניות קשת אלחוטיות עם סינון רעשים אקטיבי מושלם לחוויית שמע היקפית"),
            ("⌚ Titan Chrono SmartWatch", 1450, 18, "לייף סטייל", "שעון חכם עמיד במים, מסך אולטרה-אמוולד, ניטור מדדי בריאות מתקדם"),
            ("📱 Edge Nebula v5 Ultra", 4200, 7, "סמארטפונים", "סמארטפון העתיד, מסך מתקפל, מערך צילום קולנועי 200MP")
        ]
        cursor.executemany("INSERT INTO inventory (name, price, stock, category, description) VALUES (?, ?, ?, ?, ?)", sample_products)
        
    # הכנסת קופונים ראשוניים
    if cursor.execute("SELECT COUNT(*) FROM coupons").fetchone()[0] == 0:
        cursor.execute("INSERT INTO coupons (code, discount_percent) VALUES ('CYBER10', 10)")
        cursor.execute("INSERT INTO coupons (code, discount_percent) VALUES ('VIP20', 20)")
        
    # הגדרת משתמשי צוות כברירת מחדל
    if cursor.execute("SELECT COUNT(*) FROM staff").fetchone()[0] == 0:
        cursor.execute("INSERT INTO staff (username, pin, role) VALUES ('itay', '4444', 'admin')")
        cursor.execute("INSERT INTO staff (username, pin, role) VALUES ('delivery_boy', '1111', 'delivery')")
        
    conn.commit()
    conn.close()
    print("🎯 [Database] Enterprise tables initialized and secure data models are ready.")

