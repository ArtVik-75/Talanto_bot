from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

services_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="👩 Индивидуальная тренировка")],
        [KeyboardButton(text="🔥 Женская латина")],
        [KeyboardButton(text="👶 Детская группа")],
        [KeyboardButton(text="🏆 Переход в клуб")],
        [KeyboardButton(text="🎁 Пробное занятие")]
    ],
    resize_keyboard=True
)