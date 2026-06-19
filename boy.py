import os
import uuid
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from dotenv import load_dotenv
from generator import DRCGenerator # מייבאים את הקלאס שיצרנו

load_dotenv()
bot = Bot(token=os.getenv("BOT_TOKEN"))
dp = Dispatcher()

class DocForm(StatesGroup):
    doc_type = State()
    name = State()

@dp.message(Command("start"))
async def start(message: types.Message):
    kb = [ [types.KeyboardButton(text="אישור עבודה")], [types.KeyboardButton(text="אישור הצהרה")] ]
    await message.answer("שלום, ברוך הבא ל-DRC. מה ברצונך להפיק?", reply_markup=types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True))

@dp.message(F.text.in_(["אישור עבודה", "אישור הצהרה"]))
async def select_type(message: types.Message, state: FSMContext):
    await state.update_data(doc_type=message.text)
    await message.answer("הכנס שם מלא של המוטב:")
    await state.set_state(DocForm.name)

@dp.message(DocForm.name)
async def create_doc(message: types.Message, state: FSMContext):
    data = await state.get_data()
    doc_id = str(uuid.uuid4())[:8].upper()
    
    # הפעלת המנוע
    gen = DRCGenerator()
    filename = gen.generate(message.text, data['doc_type'], doc_id)
    
    # שליחת הקובץ
    await message.answer_document(types.FSInputFile(filename))
    os.remove(filename) # מחיקה כדי לשמור על סדר
    await state.clear()

import asyncio
asyncio.run(dp.start_polling(bot))

