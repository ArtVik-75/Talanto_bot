from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_application_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="⬅️ К списку заявок")],
        [KeyboardButton(text="🏠 Главное меню")]
    ],
    rexize_keyboard=True
)
