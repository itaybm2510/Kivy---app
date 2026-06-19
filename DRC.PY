import os
import datetime
import uuid
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from jinja2 import Template
from weasyprint import HTML
import asyncio

# טעינת הטוקן מהקובץ החיצוני
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    print("שגיאה: לא נמצא טוקן בקובץ .env")
    exit()

bot = Bot(token=TOKEN)
dp = Dispatcher()

# --- המשך הקוד כפי שסיכמנו ---
class DocState(StatesGroup):
    waiting_for_name = State()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("ברוך הבא למרכז לרישום דיגיטלי (DRC).\nבחר סוג מסמך:", 
                         reply_markup=types.ReplyKeyboardMarkup(keyboard=[
                             [types.KeyboardButton(text="אישור עבודה")],
                             [types.KeyboardButton(text="אישור הצהרה")]
                         ], resize_keyboard=True))

@dp.message(F.text.in_(["אישור עבודה", "אישור הצהרה"]))
async def ask_name(message: types.Message, state: FSMContext):
    await state.update_data(doc_type=message.text)
    await message.answer("אנא הקלד את השם המלא של בעל האישור:")
    await state.set_state(DocState.waiting_for_name)

@dp.message(DocState.waiting_for_name)
async def generate_final(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    name = message.text
    doc_id = str(uuid.uuid4())[:8].upper()
    
    with open("template.html", "r", encoding="utf-8") as f:
        template = Template(f.read())
    
    html_out = template.render(
        doc_id=f"DRC-{doc_id}",
        date=datetime.datetime.now().strftime("%d/%m/%Y"),
        title=user_data['doc_type'],
        name=name,
        body_text="הנ\"ל מוכר כפעיל במערכות המרכז לרישום דיגיטלי."
    )
    
    filename = f"DRC_{doc_id}.pdf"
    HTML(string=html_out).write_pdf(filename)
    
    await message.answer_document(types.FSInputFile(filename), caption="המסמך הופק בהצלחה על ידי DRC.")
    os.remove(filename)
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

