from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

group_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Понедельник|Среда - 18:00")]
        [KeyboardButton(text="Вторник|Четверг - 17:00")]
    ]
)