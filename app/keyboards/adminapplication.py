from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_application_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅️ К списку заявок")],
        [KeyboardButton(text="🏠 Главное меню")]
    ],
    resize_keyboard=True
)
