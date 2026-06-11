from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram import Bot

from app.keyboards.reply import main_keyboard

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в Таланто! \n\n" 
        " Выберите дейтсвие, которое вам необходимо:",
        reply_markup=main_keyboard

    )

