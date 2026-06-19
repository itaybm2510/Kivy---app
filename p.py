import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

# הגדרות הבוט
TOKEN = '8760919022:AAFkNOLNNhxWSyXmxegnXE0OfsrARFrGBMI'
YOUR_CHAT_ID = 'YOUR_CHAT_ID_HERE' # תחליף ב-ID שלך כדי לקבל התראות

# קטלוג דוגמה "מושלם"
PRODUCTS = {
    "1": {
        "name": "חבילת מיתוג לעסק",
        "price": "250₪",
        "desc": "לוגו, כרטיס ביקור ועיצוב דף נחיתה.",
        "img": "https://images.unsplash.com/photo-1524143878510-e3b8d6312402?q=80&w=500"
    },
    "2": {
        "name": "ניהול דף אינסטגרם",
        "price": "600₪",
        "desc": "3 פוסטים בשבוע + עיצוב סטורי יומי.",
        "img": "https://images.unsplash.com/photo-1611162617213-7d7a39e9b1d7?q=80&w=500"
    }
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "🚀 **ברוכים הבאים ל-DigitalBot Demo**\n\n"
        "הבוט הזה מדגים איך העסק שלכם יכול למכור אוטומטית בטלגרם.\n"
        "לחצו על הכפתור למטה כדי לראות את הקטלוג:"
    )
    keyboard = [[InlineKeyboardButton("🛍️ פתח קטלוג מוצרים", callback_query_data='view_catalog')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(welcome_text, reply_markup=reply_markup, parse_mode='Markdown')

async def show_catalog(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    
    for p_id, info in PRODUCTS.items():
        caption = f"📦 *{info['name']}*\n💰 מחיר: {info['price']}\n\n📝 {info['desc']}"
        keyboard = [[InlineKeyboardButton(f"✅ הזמן עכשיו: {info['name']}", callback_query_data=f"order_{p_id}")]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await query.message.reply_photo(photo=info['img'], caption=caption, reply_markup=reply_markup, parse_mode='Markdown')

async def handle_order(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    p_id = query.data.split('_')[1]
    product = PRODUCTS[p_id]
    user = query.from_user
    
    await query.answer("ההזמנה נשלחה!")
    await query.edit_message_caption(caption=f"✅ **תודה {user.first_name}!**\nהזמנתך ל-{product['name']} התקבלה. נציג יחזור אליך בהקדם.", parse_mode='Markdown')

    # התראה למנהל (אתה)
    admin_msg = (
        "🔔 **הזמנה חדשה התקבלה!**\n\n"
        f"👤 לקוח: {user.first_name} (@{user.username})\n"
        f"🛠️ מוצר: {product['name']}\n"
        f"💰 סכום: {product['price']}"
    )
    await context.bot.send_message(chat_id=YOUR_CHAT_ID, text=admin_msg, parse_mode='Markdown')

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(show_catalog, pattern='^view_catalog$'))
    app.add_handler(CallbackQueryHandler(handle_order, pattern='^order_'))
    
    print("בוט הדוגמה באוויר...")
    app.run_polling()

