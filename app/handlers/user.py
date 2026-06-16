from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram import Bot

from app.keyboards.reply import main_keyboard
from app.keyboards.services import services_keyboard
from app.keyboards.trainers import trainers_keyboard
from app.states.form import Form
from app.constants.services import INDIVIDUAL  
from app.google_sheets import add_application
from app.config import ADMIN_ID

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в Таланто! \n\n" 
        "Выберите дейтсвие, которое вам необходимо:",
        reply_markup=main_keyboard

    )

@router.message(F.text == "Записаться")
async def choose_service(message: Message, state: FSMContext):

    await state.set_state(Form.service)

    await message.answer(
        "Выберите интересующее вас направление:",
        reply_markup=services_keyboard
    )

@router.message(Form.service)
async def get_service(message: Message, state: FSMContext):

    await state.update_data(service=message.text)

    if message.text == INDIVIDUAL:
        
        await state.set_state(Form.trainer)

        await message.answer(
            "Выберите подходящего тренера для вас:",
            reply_markup=trainers_keyboard
        )
    
    else:
        
        await state.set_state(Form.name)

        await message.answer(
        "Введите ваше имя:",
    )

@router.message(Form.trainer)
async def get_trainer(message: Message, state: FSMContext):

    await state.update_data(trainer=message.text)

    await state.set_state(Form.name)

    await message.answer(
        "Введите ваше имя:"
    )

@router.message(Form.name)
async def get_name(message: Message, state: FSMContext):

    await state.update_data(name=message.text)

    await state.set_state(Form.age)

    await message.answer(
        "Введите ваш возраст цифрами"
    )

@router.message(Form.age)
async def get_age(message: Message, state: FSMContext):

    if not message.text.isdigit():
        return await message.answer("Ошибка! Введите ваш возраст только цирами\n\n"
                                    "Например: 25")

    await state.update_data(age=int(message.text))

    await state.set_state(Form.phone)

    await message.answer(
        "Введите ваш номер телефона в формате +7/8"
    )

@router.message(Form.phone)
async def get_phone(message: Message, state: FSMContext):

    phone = message.text.strip()

    phone = (
        phone
        .replace(" ", "")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace("+", "")
    )

    if (
        len(phone) != 11
        or not phone.isdigit()
        or not (phone.startswith("7") or phone.startswith("8"))
    ):
        return await message.answer("Ошибка! Введите, пожалуйста корректный номер телефона в формате +7 или 8 (11 цифр)")
    
    if phone.startswith("8"):
        phone = "+7" + phone[1:]
    else:
        phone = "+" + phone

    await state.update_data(phone=phone)

    await state.set_state(Form.days)

    await message.answer(
        "Какие дни вам удобны для занятий?\n\n"
        "Например: Пн, Вт, Ср или Будние дни после 18:00"
    )

@router.message(Form.days)
async def get_days(message: Message, state: FSMContext):

    await state.update_data(days=message.text)

    await state.set_state(Form.time)

    await message.answer(
        "В какое время вам будет удобно прийти на занятия?\n\n"
        "Например: в 17:00"
    )

@router.message(Form.time)
async def get_time(message: Message, state: FSMContext):

    await state.update_data(time=message.text)

    await state.set_state(Form.wishes)

    await message.answer(
        "Будут ли у вас какие-то пожелания?\n\n"
        "Например: хочу отработать связку перед турниром"
    )

@router.message(Form.wishes)
async def get_wishes(message: Message, state: FSMContext):

    await state.update_data(wishes=message.text)

    data = await state.get_data()

    trainer = data.get("trainer", "-")
    telegram_id = message.from_user.id
    username = message.from_user.username or "Не указан"

    add_application(
        username,
        telegram_id,
        data["service"],
        trainer,
        data["name"],
        data["age"],
        data["phone"],
        data["days"],
        data["time"],
        data["wishes"]
        )

    await message.answer(
        f"Спасибо за заявку! Скоро мы с вами свяжемся\n\n"
        f"Направление: {data['service']}\n"
        f"Тренер: {data['trainer']}\n\n"
        f"Имя: {data['name']}\n"
        f"Возраст: {data['age']}\n"
        f"Телефон: {data['phone']}\n\n"
        f"Дни: {data['days']}\n"
        f"Время: {data['time']}\n"
        f"Пожелания: {data['wishes']}\n\n"
    )
    
    await message.bot.send_message(
        ADMIN_ID,
        f"Новая заявка!\n\n"
        f"Username: @{username}\n"
        f"Telegram ID: {telegram_id}\n\n"
        f"Направление: {data['service']}\n"
        f"Тренер: {data['trainer']}\n\n"
        f"Имя: {data['name']}\n"
        f"Возраст: {data['age']}\n"
        f"Телефон: {data['phone']}\n\n"
        f"Дни: {data['days']}\n"
        f"Время: {data['time']}\n"
        f"Пожелания: {data['wishes']}\n\n"

    )

    await state.clear()

