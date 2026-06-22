from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

applications_pages_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅️ Назад"), KeyboardButton(text="➡️ Далее")],
        [KeyboardButton(text="🏠 Главное меню администратора")]
    ],
    resize_keyboard=True
)