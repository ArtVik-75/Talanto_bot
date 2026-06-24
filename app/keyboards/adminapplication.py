from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_application_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="🔵 Связались"), 
         KeyboardButton(text="🟢 Записан")],
        [KeyboardButton(text="🔴 Отказ")], 
        [KeyboardButton(text="⬅️ К списку заявок")],
        [KeyboardButton(text="🏠 Главное меню администратора")]
    ],
    resize_keyboard=True
)
