from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

trainers_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Светлана")],
        [KeyboardButton(text="Анастасия")],
        [KeyboardButton(text="Мария")],
        [KeyboardButton(text="Даниил")],
        [KeyboardButton(text="⬅️ Назад")]
    ],
    resize_keyboard=True
)