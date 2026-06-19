import logging
import sqlite3
import asyncio
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# --- REPORTLAB IMPORTS FOR PDF GENERATION ---
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- 🤖 CONFIG: 3-BOT ARCHITECTURE ---
SHOP_TOKEN = '8698808798:AAH9yJ9AjS4R0jZrIsvo1xAlbLjTnKl-gBA'
ADMIN_BOT_TOKEN = '8982961757:AAHVqGjuWxKRTouAVlrEI4Oaz9uqiwMVWNs'
UPDATES_BOT_TOKEN = '8758915401:AAH9cCN_X3IOR3zFAyloLjR5XBnpWiJMo2I'

ADMIN_ID = 2001911239
CORRECT_PIN = "4444"

# --- 🔄 CONVERSATION STATES ---
GET_PHONE, GET_ADDRESS, ENTER_COUPON = range(3)
AUTH_PIN, ADMIN_PANEL = range(3, 5)
# States עבור פיצ'רים חדשים של הוספת מוצרים, קופונים והוצאות
ADD_PRODUCT_NAME, ADD_PRODUCT_PRICE, ADD_PRODUCT_STOCK = range(5, 8)
ADD_COUPON_CODE, ADD_COUPON_DISCOUNT, ADD_COUPON_REF = range(8, 11)
ADD_EXPENSE_AMOUNT, ADD_EXPENSE_DESC, ADMIN_CHAT_REPLY = range(11, 14)

# --- 🗄️ DATABASE SETUP ---
def init_db():
    conn = sqlite3.connect('business_v50.db', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS inventory (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, price REAL, stock INTEGER)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, items TEXT, total REAL, 
                        method TEXT, phone TEXT, address TEXT, status TEXT DEFAULT '⏳ בהמתנה', 
                        coupon_used TEXT DEFAULT NULL, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS customers (
                        user_id INTEGER PRIMARY KEY, username TEXT, full_name TEXT, saved_phone TEXT DEFAULT NULL, 
                        saved_address TEXT DEFAULT NULL, points INTEGER DEFAULT 0)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS coupons (
                        code TEXT PRIMARY KEY, discount_percent INTEGER, used_count INTEGER DEFAULT 0, referrer_id TEXT DEFAULT NULL)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT, amount REAL, description TEXT, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    return conn, cursor

conn, cursor = init_db()
user_carts = {}
checkout_data = {}

# --- 📄 PDF GENERATION (ENGLISH) ---
def generate_pdf_invoice(order_id, customer_name, items_str, total_amount, date_str):
    filename = f"invoice_{order_id}.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter, rightMargin=30, leftMargin=30, topMargin=30, bottomMargin=30)
    story = []
    
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle('TitleStyle', parent=styles['Heading1'], fontSize=24, leading=28, textColor=colors.HexColor("#1A365D"), spaceAfter=12)
    meta_style = ParagraphStyle('MetaStyle', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor("#4A5568"))
    table_header_style = ParagraphStyle('TableHeader', parent=styles['Normal'], fontSize=11, leading=14, textColor=colors.white, fontName="Helvetica-Bold")
    table_cell_style = ParagraphStyle('TableCell', parent=styles['Normal'], fontSize=10, leading=14, textColor=colors.HexColor("#2D3748"))
    
    story.append(Paragraph("INVOICE / RECEIPT", title_style))
    story.append(Paragraph(f"<b>Invoice No:</b> #{order_id}", meta_style))
    story.append(Paragraph(f"<b>Date:</b> {date_str}", meta_style))
    story.append(Paragraph(f"<b>Customer Name:</b> {customer_name}", meta_style))
    story.append(Paragraph("<b>Business ID:</b> SmartBiz OS Enterprise (558392019)", meta_style))
    story.append(Spacer(1, 15))
    
    data = [[Paragraph("Item Description & Qty", table_header_style), Paragraph("Total Price", table_header_style)]]
    for part in items_str.split(', '):
        if part:
            data.append([Paragraph(part, table_cell_style), Paragraph("-", table_cell_style)])
            
    data.append([Paragraph("<b>Total Amount Paid:</b>", table_cell_style), Paragraph(f"<b>{total_amount} ILS</b>", table_cell_style)])
    
    t = Table(data, colWidths=[400, 120])
    t.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), colors.HexColor("#1A365D")),
        ('ALIGN', (0,0), (-1,-1), 'LEFT'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('GRID', (0,0), (-1,-1), 0.5, colors.HexColor("#CBD5E0")),
        ('BACKGROUND', (0,-1), (-1,-1), colors.HexColor("#EDF2F7")),
        ('ROWBACKGROUNDS', (0,1), (-1,-2), [colors.white, colors.HexColor("#F7FAFC")]),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('TOPPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t)
    doc.build(story)
    return filename

def get_main_menu(user_id):
    cursor.execute("SELECT points FROM customers WHERE user_id = ?", (user_id,))
    res = cursor.fetchone()
    points = res[0] if res else 0
    kb = [
        [InlineKeyboardButton("🛍️ קטלוג מוצרים", callback_data='view_catalog')],
        [InlineKeyboardButton("🛒 הסל שלי", callback_data='show_cart')],
        [InlineKeyboardButton(f"🎁 מועדון לקוחות (צברת: {points} נק')", callback_data='view_loyalty')]
    ]
    return InlineKeyboardMarkup(kb)

# --- 🛍️ CLIENT SIDE (HEBREW) ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    full_name = f"{update.effective_user.first_name} {update.effective_user.last_name or ''}".strip()
    cursor.execute("INSERT OR IGNORE INTO customers (user_id, username, full_name) VALUES (?, ?, ?)", (user_id, update.effective_user.username, full_name))
    conn.commit()
    user_carts[user_id] = []
    checkout_data[user_id] = {'discount': 0, 'coupon_code': None}
    await update.message.reply_text("💎 **ברוכים הבאים ל-SmartBiz OS Premium v50.0**\nהחנות האוטומטית שלך בטלגרם!", reply_markup=get_main_menu(user_id), parse_mode='Markdown')

async def view_catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query; await query.answer()
    cursor.execute("SELECT * FROM inventory WHERE stock > 0")
    items = cursor.fetchall()
    if not items:
        await query.message.reply_text("📋 הקטלוג ריק כרגע. מנהל המערכת יכול להוסיף מוצרים דרך בוט הניהול!")
        return
    for item in items:
        text = f"📦 **{item[1]}**\n💰 מחיר: `{item[2]}₪` | 🔥 מלאי זמין: *{item[3]}*"
        kb = [[InlineKeyboardButton("➕ הוסף לסל הקניות", callback_data=f"buy_{item[0]}")]]
        await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

async def add_to_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    item_id = query.data.split('_')[1]
    user_id = query.from_user.id
    cursor.execute("SELECT name, price, stock FROM inventory WHERE id=?", (item_id,))
    name, price, db_stock = cursor.fetchone()
    if user_id not in user_carts: user_carts[user_id] = []
    if sum(1 for i in user_carts[user_id] if i['id'] == item_id) >= db_stock:
        await query.answer("⚠️ המלאי מוגבל למוצר זה!", show_alert=True)
        return
    await query.answer("התווסף לסל!")
    user_carts[user_id].append({"id": item_id, "name": name, "price": price})
    kb = [[InlineKeyboardButton("🛒 צפה בסל והזמן", callback_data='show_cart')]]
    await query.message.reply_text(f"✅ **{name}** נוסף לסל הקניות!", reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

async def show_cart(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query; await query.answer()
    user_id = query.from_user.id
    cart = user_carts.get(user_id, [])
    if not cart:
        await query.message.reply_text("🛒 סל הקניות שלך ריק!")
        return
    subtotal = sum(i['price'] for i in cart)
    discount_pct = checkout_data.get(user_id, {}).get('discount', 0)
    total = subtotal - (subtotal * discount_pct / 100)
    
    summary = {}
    for i in cart: summary[i['name']] = summary.get(i['name'], 0) + 1
    lines = [f"• {n} x{q}" for n, q in summary.items()]
    
    text = "🛒 **סל הקניות שלך:**\n\n" + "\n".join(lines) + f"\n\n💰 מחיר ביניים: {subtotal}₪"
    if discount_pct > 0: text += f"\n🏷️ קופון פעיל: {discount_pct}% הנחה"
    text += f"\n\n💵 **סה\"כ לתשלום: {total}₪**"
    
    kb = [[InlineKeyboardButton("🎟️ הזן קוד קופון", callback_data='apply_coupon_start')],
          [InlineKeyboardButton("📱 המשך להזמנה", callback_data='checkout_details_start')]]
    await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

async def view_loyalty(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query; await query.answer()
    cursor.execute("SELECT points FROM customers WHERE user_id = ?", (query.from_user.id,))
    pts = cursor.fetchone()[0]
    await query.message.reply_text(f"🎁 **מועדון לקוחות**\nצברת עד כה: ⭐ **{pts} נקודות**\nכל רכישה מעניקה לך 10% משוויה בנקודות!")

# --- 🎟️ COUPON FLOW ---
async def apply_coupon_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text("🎟️ הזן קוד קופון:")
    return ENTER_COUPON

async def process_coupon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    code = update.message.text.strip().upper()
    cursor.execute("SELECT discount_percent, referrer_id FROM coupons WHERE code = ?", (code,))
    res = cursor.fetchone()
    if not res:
        await update.message.reply_text("❌ קופון לא תקין.")
        return ConversationHandler.END
    checkout_data[user_id]['discount'] = res[0]
    checkout_data[user_id]['coupon_code'] = code
    checkout_data[user_id]['referrer'] = res[1]
    await update.message.reply_text(f"🎉 הקופון אושר! קיבלת **{res[0]}% הנחה**", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("🛒 חזרה לסל", callback_data='show_cart')]]))
    return ConversationHandler.END

# --- 🔄 CHECKOUT FSM ---
async def checkout_details_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    user_id = update.callback_query.from_user.id
    cursor.execute("SELECT saved_phone, saved_address FROM customers WHERE user_id = ?", (user_id,))
    res = cursor.fetchone()
    if res and res[0] and res[1]:
        checkout_data[user_id]['phone'] = res[0]
        checkout_data[user_id]['address'] = res[1]
        kb = [[InlineKeyboardButton("👍 כן, השתמש בשמורים", callback_data='use_saved')],
              [InlineKeyboardButton("✏️ הזן פרטים חדשים", callback_data='force_new')]]
        await update.callback_query.message.reply_text(f"📱 להשתמש בפרטים השמורים מהזמנה קודמת?\n📞 טלפון: `{res[0]}`\n🛵 כתובת: `{res[1]}`", reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')
        return ConversationHandler.END
    await update.callback_query.message.reply_text("📞 אנא הכנס מספר טלפון למשלוח:")
    return GET_PHONE

async def get_customer_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    checkout_data[update.effective_user.id]['phone'] = update.message.text
    await update.message.reply_text("🛵 אנא הכנס כתובת מלאה למשלוח:")
    return GET_ADDRESS

async def get_customer_address(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    addr = update.message.text
    checkout_data[user_id]['address'] = addr
    cursor.execute("UPDATE customers SET saved_phone = ?, saved_address = ? WHERE user_id = ?", (checkout_data[user_id]['phone'], addr, user_id))
    conn.commit()
    await update.message.reply_text("💳 בחר אמצעי תשלום:", reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("💵 מזומן לשליח / איסוף", callback_data='pay_complete')]]))
    return ConversationHandler.END

async def checkout_complete(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query; await query.answer()
    user_id = query.from_user.id
    cart = user_carts.get(user_id, [])
    if not cart: return
    
    subtotal = sum(i['price'] for i in cart)
    details = checkout_data.get(user_id, {})
    total = subtotal - (subtotal * details.get('discount', 0) / 100)
    
    summary = {}
    for i in cart: summary[i['name']] = summary.get(i['name'], 0) + 1
    items_str = ", ".join([f"{n} (x{q})" for n, q in summary.items()])
    
    for item in cart: cursor.execute("UPDATE inventory SET stock = stock - 1 WHERE id = ?", (item['id'],))
    if details.get('coupon_code'): cursor.execute("UPDATE coupons SET used_count = used_count + 1 WHERE code = ?", (details['coupon_code'],))
    cursor.execute("UPDATE customers SET points = points + ? WHERE user_id = ?", (int(total * 0.1), user_id))
    
    cursor.execute("INSERT INTO orders (user_id, items, total, method, phone, address, coupon_used) VALUES (?, ?, ?, 'Cash', ?, ?, ?)",
                   (user_id, items_str, total, details.get('phone'), details.get('address'), details.get('coupon_code')))
    conn.commit()
    order_id = cursor.lastrowid

    admin_kb = [
        [InlineKeyboardButton("✅ אשר תשלום ושלח קבלת PDF", callback_data=f"adm_approve_{order_id}_{user_id}")],
        [InlineKeyboardButton("🔄 עדכן סטטוס משלוח", callback_data=f"adm_status_{order_id}_{user_id}")],
        [InlineKeyboardButton("💬 שלח הודעה ללקוח", callback_data=f"adm_msg_{user_id}")]
    ]
    
    admin_msg = f"🔔 **הזמנה חדשה #{order_id} הגיעה מהחנות!**\n👤 מזהה לקוח: `{user_id}`\n📦 פריטים: {items_str}\n💰 סה\"כ לגבייה: `{total}₪`"
    await Bot(token=ADMIN_BOT_TOKEN).send_message(chat_id=ADMIN_ID, text=admin_msg, reply_markup=InlineKeyboardMarkup(admin_kb), parse_mode='Markdown')
    user_carts[user_id] = []
    await query.message.reply_text(f"🎉 ההזמנה שלך התקבלה בהצלחה! מספר הזמנה: `#{order_id}`. תקבל עדכונים מבוט העדכונים שלנו.")

# --- ⚙️ PURE ADMIN BOT SIDE (FULLY RESTORED & EXTENDED) ---
def get_admin_dashboard_markup():
    kb = [
        [InlineKeyboardButton("📊 דאשבורד ונתוני עסק", callback_data='f_stats'), InlineKeyboardButton("📋 צפייה בהזמנות", callback_data='f_view_orders')],
        [InlineKeyboardButton("➕ הוספת מוצר חדש", callback_data='f_add_product'), InlineKeyboardButton("🎟️ יצירת קופון", callback_data='f_add_coupon')],
        [InlineKeyboardButton("📉 הזן הוצאה חדשה", callback_data='f_add_expense_start')]
    ]
    return InlineKeyboardMarkup(kb)

async def admin_gate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: 
        return ConversationHandler.END
    await update.message.reply_text("🔐 **מערכת אבטחה SmartBiz:**\nאנא הכנס את קוד המנהל הסודי שלך:", parse_mode='Markdown')
    return AUTH_PIN

async def admin_menu_verify(update: Update, context: ContextTypes.DEFAULT_TYPE):
    input_pin = update.message.text.strip()
    if input_pin != CORRECT_PIN:
        await update.message.reply_text("❌ קוד שגוי! הגישה נחסמה. נסה שוב:")
        return AUTH_PIN
    
    await update.message.reply_text("⚙️ **ברוך הבא לממשק הניהול הראשי!**\nהקוד אומת בהצלחה. כל האפשרויות שוחזרו ועודכנו עבורך:", reply_markup=get_admin_dashboard_markup())
    return ADMIN_PANEL

# --- ➕ NEW FEATURE: ADD PRODUCT FLOW ---
async def start_add_product(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text("📦 הזן את שם המוצר החדש:")
    return ADD_PRODUCT_NAME

async def get_product_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['new_prod_name'] = update.message.text
    await update.message.reply_text("💰 הזן מחיר בשקלים (מספר בלבד):")
    return ADD_PRODUCT_PRICE

async def get_product_price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['new_prod_price'] = update.message.text
    await update.message.reply_text("🔥 הזן כמות במלאי ההתחלתי (מספר שלם):")
    return ADD_PRODUCT_STOCK

async def get_product_stock(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        name = context.user_data['new_prod_name']
        price = float(context.user_data['new_prod_price'])
        stock = int(update.message.text)
        
        cursor.execute("INSERT INTO inventory (name, price, stock) VALUES (?, ?, ?)", (name, price, stock))
        conn.commit()
        await update.message.reply_text(f"✅ המוצר **{name}** נוסף בהצלחה לחנות וזמין לרכישה!", reply_markup=get_admin_dashboard_markup(), parse_mode='Markdown')
    except Exception:
        await update.message.reply_text("❌ שגיאה בנתונים. ודא שהמחיר והמלאי הם מספרים תקינים.", reply_markup=get_admin_dashboard_markup())
    return ADMIN_PANEL

# --- 🎟️ NEW FEATURE: ADD COUOPON FLOW ---
async def start_add_coupon(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text("🎟️ הזן את קוד הקופון החדש (למשל: VIP50):")
    return ADD_COUPON_CODE

async def get_coupon_code(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['new_cp_code'] = update.message.text.strip().upper()
    await update.message.reply_text("🏷️ הזן אחוז הנחה (מספר בין 1 ל-100):")
    return ADD_COUPON_DISCOUNT

async def get_coupon_discount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['new_cp_discount'] = update.message.text
    await update.message.reply_text("👤 הזן את שם המשפיען / שותף (או רשום 'כללי'):")
    return ADD_COUPON_REF

async def get_coupon_ref(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        code = context.user_data['new_cp_code']
        discount = int(context.user_data['new_cp_discount'])
        ref = update.message.text
        
        cursor.execute("INSERT INTO coupons (code, discount_percent, referrer_id) VALUES (?, ?, ?)", (code, discount, ref))
        conn.commit()
        await update.message.reply_text(f"✅ קופון `{code}` על סך {discount}% הנחה נוצר בהצלחה!", reply_markup=get_admin_dashboard_markup(), parse_mode='Markdown')
    except Exception:
        await update.message.reply_text("❌ שגיאה. ייתכן והקוד כבר קיים או שאחוז ההנחה לא תקין.", reply_markup=get_admin_dashboard_markup())
    return ADMIN_PANEL

# --- 📉 EXPENSE TRACKER FLOW ---
async def start_add_expense(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text("💵 הזן את סכום ההוצאה במספר בלבד:")
    return ADD_EXPENSE_AMOUNT

async def get_expense_amount(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['temp_exp_amount'] = update.message.text
    await update.message.reply_text("📝 הזן תיאור קצר עבור ההוצאה:")
    return ADD_EXPENSE_DESC

async def get_expense_desc(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        amount = float(context.user_data['temp_exp_amount'])
        desc = update.message.text
        cursor.execute("INSERT INTO expenses (amount, description) VALUES (?, ?)", (amount, desc))
        conn.commit()
        await update.message.reply_text(f"✅ ההוצאה על סך {amount}₪ נרשמה במערכת!", reply_markup=get_admin_dashboard_markup())
    except Exception:
        await update.message.reply_text("❌ חלה שגיאה בנתונים. נסה שוב.", reply_markup=get_admin_dashboard_markup())
    return ADMIN_PANEL

# --- 📄 ACTIONS & COMMUNICATION BETWEEN BOTS ---
async def handle_admin_actions(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    parts = query.data.split('_')
    
    if query.data == 'f_view_orders':
        await query.answer()
        cursor.execute("SELECT id, items, total, status FROM orders ORDER BY id DESC LIMIT 5")
        orders = cursor.fetchall()
        if not orders:
            await query.message.reply_text("📋 אין הזמנות רשומות כרגע במערכת.")
            return ADMIN_PANEL
        msg = "📋 **5 ההזמנות האחרונות בעסק:**\n\n"
        for o in orders:
            msg += f"📦 **הזמנה #{o[0]}** | סה\"כ: {o[2]}₪\nפריטים: {o[1]}\nסטטוס: *{o[3]}*\n-----------------\n"
        await query.message.reply_text(msg, parse_mode='Markdown')
        return ADMIN_PANEL

    action, uid = parts[1], parts[-1]
    
    if action == "approve":
        await query.answer("מייצר ושולח קבלת PDF אוטומטית דרך בוט העדכונים...", show_alert=True)
        order_id = parts[2]
        cursor.execute("SELECT total, items, date FROM orders WHERE id = ?", (order_id,))
        total, items, date_str = cursor.fetchone()
        cursor.execute("SELECT full_name FROM customers WHERE user_id = ?", (uid,))
        c_name = cursor.fetchone()[0]
        
        cursor.execute("UPDATE orders SET status = 'שולם ואושר ✅' WHERE id = ?", (order_id,))
        conn.commit()
        
        pdf_path = generate_pdf_invoice(order_id, c_name, items, total, date_str[:16])
        
        # 🔗 תקשורת ישירה עם בוט העדכונים (השלישי) לשליחת הודעה ללקוח
        ubot = Bot(token=UPDATES_BOT_TOKEN)
        await ubot.send_message(chat_id=int(uid), text=f"✅ **הודעה מבוט העדכונים:**\nהתשלום עבור הזמנה #{order_id} אושר! מצורפת קבלה דיגיטלית רשמית.")
        with open(pdf_path, 'rb') as pdf_file:
            await ubot.send_document(chat_id=int(uid), document=pdf_file, filename=f"Invoice_{order_id}.pdf", caption="📄 Attached is your official digital invoice.")
        os.remove(pdf_path)
        
    elif action == "msg":
        await query.answer()
        context.user_data['chat_target'] = uid
        await query.message.reply_text("💬 הקלד כעת את ההודעה שברצונך לשלוח ללקוח (ההודעה תישלח ישירות דרך בוט העדכונים):")
        return ADMIN_CHAT_REPLY
        
    elif action == "status":
        await query.answer()
        order_id = parts[2]
        context.user_data['status_order_id'] = order_id
        context.user_data['status_client_id'] = uid
        kb = [
            [InlineKeyboardButton("⏳ הזמנה בטיפול", callback_data='st_set_בטיפול ועריכה ⏳')],
            [InlineKeyboardButton("🛵 יצא עם שליח", callback_data='st_set_יצא עם השליח אליך 🛵')],
            [InlineKeyboardButton("✅ נמסר ללקוח", callback_data='st_set_נמסר בהצלחה 🎉')]
        ]
        await query.message.reply_text(f"בחר סטטוס חדש עבור הזמנה #{order_id}:", reply_markup=InlineKeyboardMarkup(kb))

async def set_order_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query; await query.answer()
    status_text = query.data.replace('st_set_', '')
    order_id = context.user_data.get('status_order_id')
    uid = context.user_data.get('status_client_id')
    
    cursor.execute("UPDATE orders SET status = ? WHERE id = ?", (status_text, order_id))
    conn.commit()
    
    await query.message.reply_text(f"✅ סטטוס הזמנה #{order_id} עודכן ל: {status_text}")
    # 🔗 בוט העדכונים מעדכן את הלקוח בזמן אמת
    await Bot(token=UPDATES_BOT_TOKEN).send_message(chat_id=int(uid), text=f"🔔 **עדכון על ההזמנה שלך מבוט העדכונים!**\nסטטוס הזמנה #{order_id} עודכן ל: **{status_text}**")

async def send_custom_client_msg(update: Update, context: ContextTypes.DEFAULT_TYPE):
    uid = context.user_data['chat_target']
    msg = update.message.text
    await Bot(token=UPDATES_BOT_TOKEN).send_message(chat_id=int(uid), text=f"💬 **הודעה רשמית מבית העסק:**\n{msg}")
    await update.message.reply_text("✅ ההודעה נשלחה בהצלחה ללקוח באמצעות בוט העדכונים!", reply_markup=get_admin_dashboard_markup())
    return ADMIN_PANEL

# --- 📊 DASHBOARD ---
async def show_stats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query; await query.answer()
    cursor.execute("SELECT SUM(total), COUNT(id) FROM orders WHERE status NOT LIKE '%מבוטל%'")
    res_orders = cursor.fetchone()
    rev = res_orders[0] or 0
    cnt = res_orders[1] or 0
    
    cursor.execute("SELECT SUM(amount) FROM expenses")
    exp = cursor.fetchone()[0] or 0
    net_profit = rev - exp
    
    cursor.execute("SELECT code, used_count, referrer_id FROM coupons")
    coupons = cursor.fetchall()
    cp_report = "\n📊 **דוח קופוני משפיענים:**\n"
    if not coupons:
        cp_report += "• אין קופונים פעילים.\n"
    for cp in coupons:
        cursor.execute("SELECT SUM(total) FROM orders WHERE coupon_used = ?", (cp[0],))
        m = cursor.fetchone()[0] or 0
        cp_report += f"• קוד: {cp[0]} ({cp[2]}) | שימושים: {cp[1]} | הכנסה: {m}₪\n"
        
    text = (
        f"📊 **דאשבורד נתוני עסק פרימיום v50.0**\n"
        f"=========================\n"
        f"💰 מחזור הכנסות ברוטו: `{rev}₪`\n"
        f"📉 סך הוצאות עסק: `{exp}₪`\n"
        f"🏆 **רווח נקי בכיס: {net_profit}₪**\n"
        f"-------------------------\n"
        f"📦 כמות הזמנות כוללת: `{cnt}`\n"
        f"{cp_report}"
        f"========================="
    )
    await query.message.reply_text(text, reply_markup=get_admin_dashboard_markup(), parse_mode='Markdown')

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE): return ConversationHandler.END

# --- 🚀 ENGINE START ---
async def main():
    # --- 🛍️ SHOP APP CONTROLLER ---
    app = ApplicationBuilder().token(SHOP_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(view_catalog, pattern='^view_catalog$'))
    app.add_handler(CallbackQueryHandler(add_to_cart, pattern='^buy_'))
    app.add_handler(CallbackQueryHandler(show_cart, pattern='^show_cart$'))
    app.add_handler(CallbackQueryHandler(view_loyalty, pattern='^view_loyalty$'))
    app.add_handler(CallbackQueryHandler(checkout_details_start, pattern='^use_saved$'))
    
    app.add_handler(ConversationHandler(
        entry_points=[CallbackQueryHandler(checkout_details_start, pattern='^checkout_details_start$'),
                      CallbackQueryHandler(get_customer_phone, pattern='^force_new$'),
                      CallbackQueryHandler(checkout_complete, pattern='^pay_complete$')],
        states={GET_PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_customer_phone)],
                GET_ADDRESS: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_customer_address)]},
        fallbacks=[CommandHandler("cancel", cancel)]
    ))
    app.add_handler(ConversationHandler(
        entry_points=[CallbackQueryHandler(apply_coupon_start, pattern='^apply_coupon_start$')],
        states={ENTER_COUPON: [MessageHandler(filters.TEXT & ~filters.COMMAND, process_coupon)]},
        fallbacks=[CommandHandler("cancel", cancel)]
    ))

    # --- ⚙️ ADMIN APP CONTROLLER (STRICT AND RICH CONVERSATION) ---
    admin_app = ApplicationBuilder().token(ADMIN_BOT_TOKEN).build()
    
    admin_handler = ConversationHandler(
        entry_points=[CommandHandler("start", admin_gate)],
        states={
            AUTH_PIN: [MessageHandler(filters.TEXT & ~filters.COMMAND, admin_menu_verify)],
            ADMIN_PANEL: [
                CallbackQueryHandler(show_stats, pattern='^f_stats$'),
                CallbackQueryHandler(handle_admin_actions, pattern='^f_view_orders$'),
                CallbackQueryHandler(start_add_product, pattern='^f_add_product$'),
                CallbackQueryHandler(start_add_coupon, pattern='^f_add_coupon$'),
                CallbackQueryHandler(start_add_expense, pattern='^f_add_expense_start$'),
                CallbackQueryHandler(handle_admin_actions, pattern='^adm_msg_')
            ],
            # מוצרים חדשים
            ADD_PRODUCT_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_product_name)],
            ADD_PRODUCT_PRICE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_product_price)],
            ADD_PRODUCT_STOCK: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_product_stock)],
            # קופונים חדשים
            ADD_COUPON_CODE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_coupon_code)],
            ADD_COUPON_DISCOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_coupon_discount)],
            ADD_COUPON_REF: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_coupon_ref)],
            # הוצאות וצ'אט לקוחות
            ADD_EXPENSE_AMOUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_expense_amount)],
            ADD_EXPENSE_DESC: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_expense_desc)],
            ADMIN_CHAT_REPLY: [MessageHandler(filters.TEXT & ~filters.COMMAND, send_custom_client_msg)]
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True
    )
    admin_app.add_handler(admin_handler)
    admin_app.add_handler(CallbackQueryHandler(handle_admin_actions, pattern='^adm_'))
    admin_app.add_handler(CallbackQueryHandler(set_order_status, pattern='^st_set_'))

    await app.initialize(); await admin_app.initialize()
    await app.start(); await admin_app.start()
    
    print("🚀 SmartBiz OS v50.0 Enterprise Is Fully Connected and Online!")
    await asyncio.gather(app.updater.start_polling(), admin_app.updater.start_polling(), asyncio.Event().wait())

if __name__ == '__main__':
    asyncio.run(main())

