from flask import render_template_string, request, redirect, jsonify, session, send_file
import json
import os
from database import get_db_connection
from views import CATALOG_TEMPLATE, CART_TEMPLATE, ADMIN_TEMPLATE
from invoice import generate_pdf_invoice

def register_routes(app, BASE_TEMPLATE):
    
    # --------------------------------------------------------
    # 1. API נועד עבור ה-Vanilla JS Core (סנכרון סל קניות מהיר)
    # --------------------------------------------------------
    @app.route('/api/cart-data')
    def get_cart_data():
        cart = session.get('cart', {})
        total_qty = sum(item['qty'] for item in cart.values())
        total_price = sum(item['price'] * item['qty'] for item in cart.values())
        return jsonify({
            'items': cart,
            'total_qty': total_qty,
            'total_price': total_price
        })

    @app.route('/add_to_cart_api/<int:product_id>')
    def add_to_cart_api(product_id):
        conn = get_db_connection()
        product = conn.execute("SELECT * FROM inventory WHERE id = ?", (product_id,)).fetchone()
        conn.close()
        
        if not product:
            return jsonify({'success': False}), 404
            
        cart = session.get('cart', {})
        p_name = product['name']
        
        if p_name in cart:
            cart[p_name]['qty'] += 1
        else:
            cart[p_name] = {
                'price': product['price'],
                'qty': 1
            }
            
        session['cart'] = cart
        session.modified = True
        
        total_qty = sum(item['qty'] for item in cart.values())
        return jsonify({'success': True, 'total_qty': total_qty})

    # --------------------------------------------------------
    # 2. נתבי חוויית לקוח (Front-Facing Hub)
    # --------------------------------------------------------
    @app.route('/')
    def index():
        conn = get_db_connection()
        products = conn.execute("SELECT * FROM inventory WHERE stock > 0").fetchall()
        conn.close()
        
        # רינדור חכם לתוך שלד ה-Bento
        rendered_content = render_template_string(CATALOG_TEMPLATE, items=products)
        return BASE_TEMPLATE.replace("CHANNELS_CONTENT_PLACEHOLDER", rendered_content)

    @app.route('/cart')
    def view_cart():
        cart = session.get('cart', {})
        discount = session.get('discount', 0)
        
        # חישוב פיננסי מדויק
        subtotal = sum(item['price'] * item['qty'] for item in cart.values())
        total = subtotal * (1 - discount / 100)
        
        rendered_content = render_template_string(CART_TEMPLATE, cart_items=cart, discount=discount, total=int(total))
        return BASE_TEMPLATE.replace("CHANNELS_CONTENT_PLACEHOLDER", rendered_content)

    @app.route('/apply_coupon', methods=['POST'])
    def apply_coupon():
        code = request.form.get('coupon', '').strip().upper()
        conn = get_db_connection()
        coupon = conn.execute("SELECT * FROM coupons WHERE code = ?", (code,)).fetchone()
        conn.close()
        
        if coupon:
            session['discount'] = coupon['discount_percent']
        else:
            session['discount'] = 0
            
        session.modified = True
        return redirect('/cart')

    @app.route('/checkout', methods=['POST'])
    def checkout():
        cart = session.get('cart', {})
        if not cart:
            return redirect('/')
            
        name = request.form.get('name')
        phone = request.form.get('phone')
        address = request.form.get('address')
        discount = session.get('discount', 0)
        
        subtotal = sum(item['price'] * item['qty'] for item in cart.values())
        total = int(subtotal * (1 - discount / 100))
        
        # יצירת מחרוזת מובנית של הפריטים עבור מסד הנתונים
        items_list = [f"{k} (x{v['qty']})" for k, v in cart.items()]
        items_str = ", ".join(items_list)
        
        conn = get_db_connection()
        # 1. עדכון כמות מלאי זמין פיזית בטבלה
        for k, v in cart.items():
            conn.execute("UPDATE inventory SET stock = stock - ? WHERE name = ? AND stock >= ?", (v['qty'], k, v['qty']))
            
        # 2. רישום ההזמנה במערכת ה-CRM
        cursor = conn.cursor()
        cursor.execute("INSERT INTO orders (items, total, phone, address, status) VALUES (?, ?, ?, ?, '⏳ בהמתנה לניהול')",
                       (items_str, total, phone, f"{name} - {address}"))
        conn.commit()
        conn.close()
        
        # ניקוי סל הקניות הנוכחי
        session.pop('cart', None)
        session.pop('discount', None)
        
        return BASE_TEMPLATE.replace("CHANNELS_CONTENT_PLACEHOLDER", f"""
            <div class="max-w-md mx-auto text-center py-16 animate-fade-in">
                <div class="glass-panel p-8 rounded-3xl bento-glow-green">
                    <span class="text-4xl">🚀</span>
                    <h2 class="text-xl font-black mt-4 text-emerald-400">ההזמנה נקלטה במערכת בהצלחה!</h2>
                    <p class="text-slate-400 text-xs mt-2 leading-relaxed">
                        מנהל המערכת יעבור על הפרטים כעת. החשבונית המאובטחת תונפק בקונסולת הניהול מיד עם אישור המשלוח.
                    </p>
                    <a href="/" class="mt-6 inline-block bg-slate-900 border border-white/5 px-6 py-2 rounded-xl text-xs font-bold text-slate-300 hover:text-white transition">חזרה לחנות</a>
                </div>
            </div>
        """)

    # --------------------------------------------------------
    # 3. קונסולת ניהול ארגונית (Backoffice CRM & Financials)
    # --------------------------------------------------------
    @app.route('/admin')
    def admin_panel():
        conn = get_db_connection()
        orders = conn.execute("SELECT * FROM orders ORDER BY id DESC").fetchall()
        
        # חישוב נתוני אנליטיקה בזמן אמת לגרפים
        total_revenue = conn.execute("SELECT SUM(total) FROM orders WHERE status != '❌ מבוטל'").fetchone()[0] or 0
        total_expenses = conn.execute("SELECT SUM(amount) FROM expenses").fetchone()[0] or 0
        net_profit = total_revenue - total_expenses
        
        stats = {
            'rev': int(total_revenue),
            'exp': int(total_expenses),
            'net': int(net_profit)
        }
        
        conn.close()
        rendered_content = render_template_string(ADMIN_TEMPLATE, orders=orders, stats=stats)
        return BASE_TEMPLATE.replace("CHANNELS_CONTENT_PLACEHOLDER", rendered_content)

    @app.route('/admin/approve/<int:order_id>')
    def approve_order(order_id):
        conn = get_db_connection()
        order = conn.execute("SELECT * FROM orders WHERE id = ?", (order_id,)).fetchone()
        
        if order:
            # עדכון סטטוס ב-CRM
            conn.execute("UPDATE orders SET status = '✅ מאושר ומודפס' WHERE id = ?", (order_id,))
            conn.commit()
            
            # הפקת קובץ PDF בצורה אוטומטית דרך המודול המשודרג
            pdf_path = generate_pdf_invoice(order['id'], order['items'], order['total'], str(order['date'])[:10])
            conn.close()
            return send_file(pdf_path, as_attachment=True)
            
        conn.close()
        return redirect('/admin')

    @app.route('/admin/update_status/<int:order_id>/<string:new_status>')
    def update_status(order_id, new_status):
        conn = get_db_connection()
        conn.execute("UPDATE orders SET status = ? WHERE id = ?", (new_status, order_id))
        conn.commit()
        conn.close()
        return redirect('/admin')

    @app.route('/admin/add_product', methods=['POST'])
    def add_product():
        name = request.form.get('name')
        category = request.form.get('category')
        price = float(request.form.get('price'))
        stock = int(request.form.get('stock'))
        description = request.form.get('description')
        
        conn = get_db_connection()
        conn.execute("INSERT INTO inventory (name, category, price, stock, description) VALUES (?, ?, ?, ?, ?)",
                     (name, category, price, stock, description))
        conn.commit()
        conn.close()
        return redirect('/admin')

    @app.route('/admin/add_expense', methods=['POST'])
    def add_expense():
        amount = float(request.form.get('amount'))
        description = request.form.get('desc')
        
        conn = get_db_connection()
        conn.execute("INSERT INTO expenses (amount, description) VALUES (?, ?)", (amount, description))
        conn.commit()
        conn.close()
        return redirect('/admin')

    # --------------------------------------------------------
    # 4. 🤖 מנוע צ'אטבוט ה-AI הפנימי של חברת הענק (Context-Aware)
    # --------------------------------------------------------
    @app.route('/api/ai-chat')
    def ai_chat():
        user_query = request.args.get('q', '').lower().strip()
        if not user_query:
            return jsonify({'response': 'שלום! שאל אותי כל שאלה על פריטים במלאי או קופונים.'})
            
        conn = get_db_connection()
        products = conn.execute("SELECT name, price, stock, category, description FROM inventory").fetchall()
        coupons = conn.execute("SELECT code, discount_percent FROM coupons").fetchall()
        conn.close()
        
        # אלגוריתם זיהוי חכם מבוסס מילות מפתח והצלבה דינמית של מסד הנתונים
        
        # בדיקה 1: האם המשתמש מחפש מחשב / חומרה
        if 'מחשב' in user_query or 'laptop' in user_query or 'cyberbook' in user_query:
            p = products[0] # CyberBook
            return jsonify({'response': f"💻 מצאתי עבורך את קצה הטכנולוגיה: <b>{p['name']}</b>.<br>זהו {p['description']}.<br>💰 מחיר פרימיום: {p['price']}₪ (זמין כעת במלאי: {p['stock']} יחידות). תרצה להוסיף אותו?"})
            
        # בדיקה 2: האם מחפש אוזניות / סאונד
        if 'אוזניות' in user_query or 'סאונד' in user_query or 'שמע' in user_query:
            p = products[1] # Quantum Sound
            return jsonify({'response': f"🎧 לחובבי סאונד איכותי: מומלץ על <b>{p['name']}</b>.<br>{p['description']}.<br>💰 מחיר מיוחד: {p['price']}₪ (נשארו רק {p['stock']} במלאי)."})
            
        # בדיקה 3: האם מחפש שעון / סגנון
        if 'שעון' in user_query or 'watch' in user_query or 'לייף' in user_query:
            p = products[2] # SmartWatch
            return jsonify({'response': f"⌚ בשבילך, הדגם המבוקש ביותר: <b>{p['name']}</b>.<br>{p['description']}.<br>💰 עלות: {p['price']}₪. מושלם ליומיום ולספורט תחרותי."})

        # בדיקה 4: האם מחפש טלפון / סמארטפון
        if 'טלפון' in user_query or 'סלולרי' in user_query or 'סמארטפון' in user_query:
            p = products[3] # Phone
            return jsonify({'response': f"📱 מכשיר הדגל הבא שלך: <b>{p['name']}</b>.<br>{p['description']}.<br>💰 מחיר: {p['price']}₪ (המלאי מוגבל ביותר: רק {p['stock']} יחידות!)."})

        # בדיקה 5: האם שאל על קופונים או הנחות
        if 'קופון' in user_query or 'הנחה' in user_query or 'מבצע' in user_query:
            coupon_list = [f"<b>{c['code']}</b> הנותן {c['discount_percent']}% הנחה" for c in coupons]
            return jsonify({'response': f"🏷️ מצאתי קודים פעילים במערכת עבורך! בקופה תוכל להזין: {', '.join(coupon_list)}. תהנה!"})
            
        # מענה ברירת מחדל חכם במידה ולא נמצאה התאמה ישירה
        return jsonify({'response': "🤖 אני מכיר את כל המוצרים של איתי בחנות. נסה לשאול אותי על 'מחשב', 'אוזניות', 'טלפון', או לבקש 'קופון'!"})

