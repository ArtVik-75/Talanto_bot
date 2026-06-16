from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

latina_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📅 Понедельник")],
        [KeyboardButton(text="📅 Четверг")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)