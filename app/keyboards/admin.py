from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📋 Заявки")],
        [KeyboardButton(text="📊 Статистика")],
        [KeyboardButton(text="🏠 Главное меню")]
    ],
    resize_keyboard=True
)