from aiogram import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="💃 Записаться")],
        [KeyboardButton(text="📅 Расписание")],
        [KeyboardButton(text="🏆 О клубе")],
        [KeyboardButton(text="📞 Контакты")]
    ],
    resize_keyboard=True
)