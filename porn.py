import logging
import sqlite3
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes

# הגדרת לוגים למעקב בטרמקס
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# --- ⚙️ קונפיגורציית טוקנים ו-ID רשמיים ---
SHOP_TOKEN = '8957239010:AAE6OPPUWh0PjiYF3l_ca3SzeWW8n7yZlyk'   # בוט 1: חלון הראווה הציבורי
ADMIN_TOKEN = '8670755375:AAGibRDpy4SVO0SVNfW1PoWwQxry8sFpQ2U'  # בוט 2: חמ"ל מנהלים
GATE_TOKEN = '8864510234:AAGm1i2vAU996Cz96rTyORqPGU3uSrxkmJY'   # בוט 3: שער הגישה לקבוצות

ADMIN_ID = 2001911239  # ה-ID הפיזי שלך כמנהל על

# --- 🔗 הגדרת קישורי הקבוצות הפרטיות שלך ---
GROUP_LINK_ISRAEL = "https://t.me/+rW-E5tzQAO9lNDU0" # הקישור המאובטח שלך
GROUP_LINK_OMEGLE = "https://t.me/+Example_Omegle_Group" # זמני

# כתובות ארנקי הקריפטו
BTC_WALLET = "bc1qtaf5tek80su9kct7ndclmypjgavmkehy8evmwt"
ETH_WALLET = "0xfafc438a1c073f7ef21da7bb1b0626b96def76bc"
USDT_WALLET = "0xfafc438a1c073f7ef21da7bb1b0626b96def76bc"

# --- 🗄️ אתחול בסיס הנתונים ---
def init_db():
    conn = sqlite3.connect('pornyard.db', check_same_thread=False)
    cursor = conn.cursor()
    # טבלת מנויים מאושרים
    cursor.execute('''CREATE TABLE IF NOT EXISTS vip_members (user_id INTEGER PRIMARY KEY, approved_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    # טבלת מעקב לקוחות כללית
    cursor.execute('''CREATE TABLE IF NOT EXISTS tracked_users (user_id INTEGER PRIMARY KEY, username TEXT, first_name TEXT, joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    # טבלת פניות פתוחות למניעת ספאם (חדש!)
    cursor.execute('''CREATE TABLE IF NOT EXISTS open_tickets (user_id INTEGER PRIMARY KEY, created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    return conn, cursor

conn, cursor = init_db()
user_selections = {}

# =====================================================================
# 🤖 בוט 1: חלון הראווה הציבורי (Pornyard Israel)
# =====================================================================
async def shop_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    username = update.effective_user.username or "NoUsername"
    first_name = update.effective_user.first_name or "User"
    
    cursor.execute("INSERT OR IGNORE INTO tracked_users (user_id, username, first_name) VALUES (?, ?, ?)", (user_id, username, first_name))
    conn.commit()
    
    text = (
        f"🔥 **ברוך הבא ל-Pornyard Israel — עולם הניודסים הרשמי!** 🔥\n\n"
        f"המאגר המרכזי והגדול ביותר שמלכד את כל החומרים הכי חמים במדינה במקום אחד. "
        f"בלי צנזורות, בלי לינקים שבורים ובלי משחקים.\n\n"
        f"🔒 *המערכת מאובטחת, אנונימית ודיסקרטית לחלוטין.*\n\n"
        f"👇 **בחר קטגוריה לצפייה בפרטים ורכישת גישה מיידית:**"
    )
    
    kb = [
        [InlineKeyboardButton("🔞 ישראליות וניודסים (סרטונים בלעדיים)", callback_data='cat_israel')],
        [InlineKeyboardButton("🎥 אומיגל (סרטוני האומיגל החמים במדינה)", callback_data='cat_omegle')],
        [InlineKeyboardButton("👑 מועדון הכל כלול (הדיל המשתלם ביותר)", callback_data='cat_all')]
    ]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

async def handle_categories(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query; await query.answer()
    user_id = query.from_user.id
    data = query.data
    
    if data == 'cat_israel':
        user_selections[user_id] = {"item": "🔞 ישראליות וניודסים", "price": "50 ₪"}
        text = (
            f"🔞 **מאגר הישראליות והניודסים המלא — VIP**\n\n"
            f"כל הסרטונים הבלעדיים שהודלפו, ניודסים חמים וישראליות ברמה הגבוהה ביותר במדינה. "
            f"תוכן אקסקלוסיבי לחברי המועדון בלבד. המאגר מתעדכן באופן קבוע!\n\n"
            f"💰 **מחיר גישה קבועה לקבוצה:** `50 ₪`"
        )
    elif data == 'cat_omegle':
        user_selections[user_id] = {"item": "🎥 סרטוני אומיגל", "price": "50 ₪"}
        text = (
            f"🎥 **קטגוריית אומיגל הבלעדית — VIP**\n\n"
            f"כל סרטוני האומיגל החמים במדינה. השיחות הכי מעניינות, הרגעים המטורפים והחומרים "
            f"הבלעדיים שעלו בצ'אט וידאו, מתועדים באיכות הגבוהה ביותר וללא שום מסכים שחורים.\n\n"
            f"💰 **מחיר גישה קבועה לקבוצה:** `50 ₪`"
        )
    elif data == 'cat_all':
        user_selections[user_id] = {"item": "👑 מועדון הכל כלול (חבילה משולבת)", "price": "80 ₪"}
        text = (
            f"👑 **מנוי זהב — גישה מלאה לכל העולמות!**\n\n"
            f"כרטיס כניסה קבוע ושילוב מנצח לכל הקבוצות הפרטיות שלנו: ישראליות וניודסים ברמה הגבוהה ביותר, "
            f"וכל סרטוני האומיגל החמים במדינה במחיר מטורף.\n\n"
            f"💰 **מחיר חבילה משולבת (הכל כלול):** `80 ₪` *(במקום 100 ₪)*"
        )
        
    kb = [[InlineKeyboardButton("💳 המשך לרכישה ופרטי תשלום", callback_data='go_checkout')]]
    await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

async def go_checkout(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query; await query.answer()
    user_id = query.from_user.id
    
    selection = user_selections.get(user_id, {"item": "מנוי גישה קבוע", "price": "בהתאם לקטגוריה"})
    
    text = (
        f"🔒 **אזור רכישה דיסקרטי ומאובטח**\n\n"
        f"📌 **ההזמנה שלך:** {selection['item']}\n"
        f"💰 **סכום לתשלום:** `{selection['price']}`\n\n"
        f"לחץ על הכתובת למטה כדי להעתיק אותה אוטומטית:\n"
        f"🪙 **Bitcoin (BTC):**\n`{BTC_WALLET}`\n\n"
        f"💎 **Ethereum (ETH):**\n`{ETH_WALLET}`\n\n"
        f"💵 **USDT (ERC-20):**\n`{USDT_WALLET}`\n\n"
        f"⏱️ **לאחר שביצעת את ההעברה בארנק שלך:**\n"
        f"לחץ על הכפתור הירוק למטה כדי לפתוח פנייה רשמית אצל ההנהלה. "
        f"הבוט ישלח למנהל את פרטי ההזמנה שלך, והמנהל יפנה אליך מיד בצ'אט כדי לקבל את צילום המסך ולאשר אותך!"
    )
    
    kb = [[InlineKeyboardButton("✅ שילמתי! פתח פנייה אצל ההנהלה", callback_data='open_ticket')]]
    await query.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

# פתיחת פנייה מוגנת מספאם
async def open_ticket(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query; await query.answer()
    user_id = query.from_user.id
    username = query.from_user.username or "אין יוזר"
    first_name = query.from_user.first_name or "User"
    
    # הגנה מספאם: בדיקה אם יש כבר פנייה פתוחה בבסיס הנתונים
    cursor.execute("SELECT 1 FROM open_tickets WHERE user_id = ?", (user_id,))
    already_has_ticket = cursor.fetchone()
    
    if already_has_ticket:
        spam_text = (
            f"⚠️ **כבר פתחת פנייה במערכת!**\n\n"
            f"אין צורך ללחוץ פעמיים. פניית הרכישה שלך נמצאת בטיפול אצל המנהל כרגע. "
            f"אנא המתן בסבלנות, המנהל יפנה אליך בהקדם האפשרי בצ'אט הפרטי."
        )
        await query.message.reply_text(spam_text, parse_mode='Markdown')
        return

    selection = user_selections.get(user_id, {"item": "לא נבחר", "price": "לא נבחר"})
    
    # רישום הפנייה כדי לחסום אותו ללחיצה הבאה
    cursor.execute("INSERT OR IGNORE INTO open_tickets (user_id) VALUES (?)", (user_id,))
    conn.commit()
    
    # הודעה נקייה ללא parse_mode - חסינה לחלוטין מקריסות טקסט!
    admin_bot = Bot(token=ADMIN_TOKEN)
    admin_text = (
        f"📥 פניית רכישה חדשה נפתחה\n\n"
        f"👤 שם לקוח: {first_name}\n"
        f"💬 יוזר טלגרם: @{username}\n"
        f"🆔 מזהה משתמש (User ID): {user_id}\n\n"
        f"📦 הפריט שהוזמן: {selection['item']}\n"
        f"💵 סכום לתשלום: {selection['price']}\n\n"
        f"💡 מה לעשות עכשיו?\n"
        f"לחץ על הכפתור למטה לפתיחת הצ'אט הפרטי איתו, בקש צילום מסך של העברה, ולאישור שלח כאן פקודה בדיוק ככה:\n"
        f"add {user_id}"
    )
    
    admin_kb = [[InlineKeyboardButton(f"💬 פתח צ'אט פרטי", url=f"tg://user?id={user_id}")]]
    await admin_bot.send_message(chat_id=ADMIN_ID, text=admin_text, reply_markup=InlineKeyboardMarkup(admin_kb))
    
    client_text = (
        f"✅ **הפנייה שלך נפתחה בהצלחה אצל ההנהלה!**\n\n"
        f"הודעה מסודרת עם פרטי ה-ID שלך וההזמנה הועברה למנהל הראשי.\n"
        f"המנהל יפנה אליך בדקות הקרובות בצ'אט הפרטי כדי לקבל את צילום המסך של ההעברה ולהפעיל לך את הגישה. נא להישאר זמין!"
    )
    await query.message.reply_text(client_text, parse_mode='Markdown')

# =====================================================================
# ⚙️ בוט 2: חמ"ל הניהול והמנהלים (רק בשבילך)
# =====================================================================
async def admin_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    cursor.execute("SELECT COUNT(*) FROM vip_members")
    vip_count = cursor.fetchone()[0]
    
    text = (
        f"⚙️ **חמ\"ל ניהול Pornyard Israel פעיל!**\n\n"
        f"👑 מנויי VIP מאושרים ופעילים כרגע: `{vip_count}`\n\n"
        f"✏️ **איך לאשר לקוח לאחר שבדקת קבלה?**\n"
        f"שלח פשוט: `add USER_ID`"
    )
    await update.message.reply_text(text, parse_mode='Markdown')

async def admin_process_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ADMIN_ID: return
    msg = update.message.text.strip()
    
    if msg.startswith("add "):
        try:
            target_id = int(msg.split(" ")[1])
            cursor.execute("INSERT OR IGNORE INTO vip_members (user_id) VALUES (?)", (target_id,))
            
            # מחיקת הפנייה הפתוחה מטבלת הספאם ברגע שהוא אושר
            cursor.execute("DELETE FROM open_tickets WHERE user_id = ?", (target_id,))
            conn.commit()
            
            gate_bot = Bot(token=GATE_TOKEN)
            alert_text = (
                f"🎉 **המנוי שלך אושר והופעל בהצלחה על ידי המנהל!**\n\n"
                f"כעת נפתחה לך הגישה המלאה לקבוצות התוכן הסגורות.\n"
                f"לחץ על הכפתור `/start` כאן בבוט כדי לקבל את קישורי הכניסה האישיים שלך!"
            )
            await gate_bot.send_message(chat_id=target_id, text=alert_text, parse_mode='Markdown')
            await update.message.reply_text(f"✅ משתמש `{target_id}` אושר במערכת, ופנייתו נסגרה!")
        except Exception as e:
            await update.message.reply_text(f"❌ תקלה ברישום: {e}")

# =====================================================================
# 🤖 בוט 3: שער הגישה לקבוצות ה-VIP (לרשומים בלבד)
# =====================================================================
async def gate_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    cursor.execute("SELECT 1 FROM vip_members WHERE user_id = ?", (user_id,))
    if not cursor.fetchone():
        await update.message.reply_text("🔒 **הגישה חסומה!**\n\nבוט זה משמש כשער גישה מאובטח לחברי מועדון ה-VIP בלבד.", parse_mode='Markdown')
        return
        
    text = (
        f"👑 **ברוך הבא למועדון ה-VIP הרשמי של Pornyard Israel!**\n\n"
        f"להלן קישורי הגישה האישיים שלך לקבוצות התוכן הסגורות:\n\n"
        f"⚠️ *שים לב:* הקבוצות דורשות 'בקשת הצטרפות'. ברגע שתלחץ המערכת תאשר אותך מיידית!"
    )
    kb = [
        [InlineKeyboardButton("🔞 קבוצה 1: ישראליות וניודסים בלעדיים", url=GROUP_LINK_ISRAEL)],
        [InlineKeyboardButton("🎥 קבוצה 2: סרטוני אומיגל החמים במדינה", url=GROUP_LINK_OMEGLE)]
    ]
    await update.message.reply_text(text, reply_markup=InlineKeyboardMarkup(kb), parse_mode='Markdown')

# =====================================================================
# 🚀 מנוע ההרצה
# =====================================================================
async def main():
    shop_app = ApplicationBuilder().token(SHOP_TOKEN).build()
    shop_app.add_handler(CommandHandler("start", shop_start))
    shop_app.add_handler(CallbackQueryHandler(handle_categories, pattern='^cat_'))
    shop_app.add_handler(CallbackQueryHandler(go_checkout, pattern='^go_checkout$'))
    shop_app.add_handler(CallbackQueryHandler(open_ticket, pattern='^open_ticket$'))
    
    admin_app = ApplicationBuilder().token(ADMIN_TOKEN).build()
    admin_app.add_handler(CommandHandler("start", admin_start))
    admin_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, admin_process_command))
    
    gate_app = ApplicationBuilder().token(GATE_TOKEN).build()
    gate_app.add_handler(CommandHandler("start", gate_start))

    await shop_app.initialize(); await admin_app.initialize(); await gate_app.initialize()
    await shop_app.start(); await admin_app.start(); await gate_app.start()
    
    print("🔥 מנוע נגד ספאם 2.2 באוויר ב-Termux ומאובטח מקריסות!")
    await asyncio.gather(shop_app.updater.start_polling(), admin_app.updater.start_polling(), gate_app.updater.start_polling(), asyncio.Event().wait())

if __name__ == '__main__':
    asyncio.run(main())

