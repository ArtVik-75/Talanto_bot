from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

experience_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="✅ Есть опыт")],
        [KeyboardButton(text="❌ Нет опыта")]
    ],
    resize_keyboard=True
)