from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram import Bot

from app.keyboards.reply import main_keyboard
from app.keyboards.services import services_keyboard
from app.keyboards.trainers import trainers_keyboard
from app.keyboards.latina import latina_keyboard
from app.keyboards.experience import experience_keyboard
from app.keyboards.menu import menu_keyboard
from app.keyboards.group import group_keyboard
from app.keyboards.admin import admin_keyboard
from app.keyboards.adminapplication import admin_application_keyboard
from app.states.form import Form
from app.states.adminform import AdminForm
from app.constants.services import INDIVIDUAL
from app.constants.services import LATINA
from app.constants.services import CHILDREN
from app.constants.services import TRANSFER
from app.google_sheets import add_application, get_all_applications
from app.config import ADMIN_ID

router = Router()

@router.message(Command("admin"))
async def admin_test(message: Message):

    if message.from_user.id != ADMIN_ID:

        return await message.answer(
            "❌ Доступ запрещен"
        )

    await message.answer(
        "⚙️ Панель администратора",
        reply_markup=admin_keyboard
    )

@router.message(F.text == "📋 Заявки")
async def admin_applications(message: Message, state: FSMContext):

    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Доступ запрещен")
    
    applications = get_all_applications()

    last_applications = applications[-10:]

    text = "📋 Последние заявки\n\n"

    for number, application in enumerate(last_applications, start=1):

        text += (
            f"{number}. {application['Имя']} | "
            f"{application['Услуга']} | "
            f"{application['Дата']}\n"
        )

    await message.answer(text)

    await state.set_state(AdminForm.application_number)

    await message.answer("Введите номер заявки для просмотра подробной информации:")


@router.message(AdminForm.application_number)
async def admim_application_details(message: Message, state: FSMContext):

    if message.text == "🏠 Главное меню":
        await state.clear()

        return await message.answer(
            "Главное меню администратора:",
            reply_markup=admin_keyboard
        )

    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Доступ запрещен")
    
    if not message.text.isdigit():
        return await message.answer("Ошибка! Введите номер заявки цифрами")
    
    application_number = int(message.text)

    applications = get_all_applications()
    last_applications = applications[-10:]

    if application_number < 1 or application_number > len(last_applications):
        return await message.answer("Ошибка! Введите корректный номер заявки из списка")
    
    application = last_applications[application_number -1]

    text = (
        f"📋 Заявка\n\n"
        f"Telegram ID: {application['Telegram ID']}\n"
        f"Username: {application['Username']}\n"
        f"👤 Имя: {application['Имя']}\n"
        f"👨‍👩‍👦 Имя ребенка: {application['Имя ребенка']}\n"
        f"📚 Услуга: {application['Услуга']}\n"
        f"📅 Дата: {application['Дата']}\n"
        f"📞 Телефон: {application['Телефон']}\n"
        f"🎓 Опыт: {application['Опыт']}\n"
        f"📝 Об опыте: {application['Об опыте']}\n"
        f"🏆 Причина перехода: {application['Причина перехода']}"
    )

    await message.answer(text, reply_markup=admin_application_keyboard)

    await state.clear()
    

@router.message(F.text == "📊 Статистика")
async def admin_stats(message: Message, state: FSMContext):
    
    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Доступ запрещен")
    
    await message.answer("📊 Раздел статистики")

@router.message(F.text == "🏠 Главное меню")
async def admin_exit(message: Message, state: FSMContext):

    if message.from_user.id != ADMIN_ID:
        return await message.answer("❌ Доступ запрещен")
    
    await state.clear()
    
    await message.answer(
        "Главное меню",
        reply_markup=menu_keyboard
    )


@router.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        "Добро пожаловать в Таланто! \n\nВыберите дейтсвие, которое вам необходимо:",
        reply_markup=main_keyboard,
    )


@router.message(F.text == "🏠 Главное меню")
async def back_to_menu(message: Message, state: FSMContext):

    await state.clear()

    await message.answer("Выберите действие:", reply_markup=main_keyboard)


@router.message(F.text == "📅 Расписание")
async def schedule(message: Message):

    await message.answer(
        "📅 Расписание занятий\n\n"
        "🔥 Женская латина\n"
        "• Понедельник — 20:00\n"
        "• Четверг — 20:00\n\n"
        "👶 Детская группа\n"
        "• Вторник — 18:00\n"
        "• Пятница — 18:00\n\n"
        "👩 Индивидуальные тренировки\n"
        "• По согласованию с тренером",
        reply_markup=menu_keyboard,
    )


@router.message(F.text == "🏆 О клубе")
async def about(message: Message):

    await message.answer(
        "Школа танцев ТАЛАНТО — это пространство для развития, творчества и любви к танцу.\n\n"
        "Мы работаем с детьми и взрослыми, проводим групповые и индивидуальные занятия, готовим спортсменов к соревнованиям и помогаем каждому раскрыть свой потенциал.\n\n"
        "Наши направления:\n"
        "• Женская латина\n"
        "• Детские группы\n"
        "• Индивидуальные тренировки\n"
        "• Подготовка спортсменов\n\n"
        "Будем рады видеть вас на занятиях ❤️",
        reply_markup=menu_keyboard,
    )


@router.message(F.text == "📞 Контакты")
async def contact(message: Message):

    await message.answer(
        "📍 Адрес:\n"
        "ул. Багульниковая 35\n\n"
        "📞 Телефон:\n"
        "+7 ...\n"
        "📱 Telegram:\n"
        "@...\n"
        "📷 Instagram:\n"
        "...\n"
        "🕒 Время работы:\n"
        "ежедневно с 10:00\n",
        reply_markup=menu_keyboard,
    )


@router.message(F.text == "💃 Записаться")
async def choose_service(message: Message, state: FSMContext):

    await state.set_state(Form.service)

    await message.answer(
        "Выберите интересующее вас направление:", reply_markup=services_keyboard
    )


@router.message(Form.service)
async def get_service(message: Message, state: FSMContext):

    await state.update_data(service=message.text)

    if message.text == INDIVIDUAL:
        await state.set_state(Form.trainer)

        await message.answer(
            "Выберите подходящего тренера для вас:", reply_markup=trainers_keyboard
        )

    elif message.text == LATINA:
        await state.update_data(trainer="-")
        await state.set_state(Form.name)

        await message.answer("Введите ваше имя:", reply_markup=menu_keyboard)

    elif message.text == CHILDREN:
        await state.update_data(trainer="-")
        await state.set_state(Form.name)

        await message.answer("Введите имя родителя:", reply_markup=menu_keyboard)

    elif message.text == TRANSFER:
        await state.update_data(trainer="-")
        await state.set_state(Form.name)

        await message.answer("Введите ваше имя:", reply_markup=menu_keyboard)

    else:
        await state.set_state(Form.name)

        await message.answer("Введите ваше имя:", reply_markup=menu_keyboard)


@router.message(Form.trainer)
async def get_trainer(message: Message, state: FSMContext):

    await state.update_data(trainer=message.text)

    await state.set_state(Form.name)

    await message.answer("Введите ваше имя:", reply_markup=menu_keyboard)


@router.message(Form.name)
async def get_name(message: Message, state: FSMContext):

    await state.update_data(name=message.text)

    data = await state.get_data()

    if data["service"] == CHILDREN:
        await state.set_state(Form.child_name)

        await message.answer("Введите имя ребенка:", reply_markup=menu_keyboard)

    else:
        await state.set_state(Form.age)

        await message.answer("Введите ваш возраст цифрами:", reply_markup=menu_keyboard)


@router.message(Form.child_name)
async def get_child_name(message: Message, state: FSMContext):

    await state.update_data(child_name=message.text)

    await state.set_state(Form.age)

    await message.answer("Введите возраст ребенка:", reply_markup=menu_keyboard)


@router.message(Form.age)
async def get_age(message: Message, state: FSMContext):

    data = await state.get_data()

    if not message.text.isdigit():
        return await message.answer(
            "Ошибка! Введите возраст только цирами\n\nНапример: 25"
        )

    await state.update_data(age=int(message.text))

    await state.set_state(Form.experience)

    if data["service"] == CHILDREN:
        await message.answer(
            "Есть ли у ребенка танцевальный опыт?", reply_markup=experience_keyboard
        )

    else:
        await message.answer(
            "Есть ли у вас танцевальный опыт?", reply_markup=experience_keyboard
        )


@router.message(Form.experience)
async def get_experience(message: Message, state: FSMContext):

    if message.text == "✅ Есть опыт":
        await state.update_data(experience="Есть")

        await state.set_state(Form.experience_details)

        await message.answer(
            "Расскажите кратко о танцевальном опыте:", reply_markup=menu_keyboard
        )

    elif message.text == "❌ Нет опыта":
        await state.update_data(experience=message.text)
        await state.update_data(experience_details="-")

        await state.set_state(Form.phone)

        await message.answer(
            "Введите ваш номер телефона в формате +7/8 (11 цифр)",
            reply_markup=menu_keyboard,
        )

    else:

        await message.answer(
            "Пожалуйста, воспользуйтесь кнопками ниже", reply_markup=experience_keyboard
        )


@router.message(Form.experience_details)
async def get_experience_details(message: Message, state: FSMContext):

    await state.update_data(experience_details=message.text)

    await state.set_state(Form.phone)

    await message.answer(
        "Введите ваш номер телефона в формате +7/8 (11 цифр)",
        reply_markup=menu_keyboard,
    )


@router.message(Form.phone)
async def get_phone(message: Message, state: FSMContext):

    phone = message.text.strip()

    phone = (
        phone.replace(" ", "")
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
        return await message.answer(
            "Ошибка! Введите, пожалуйста корректный номер телефона в формате +7 или 8 (11 цифр)"
        )

    if phone.startswith("8"):
        phone = "+7" + phone[1:]
    else:
        phone = "+" + phone

    await state.update_data(phone=phone)

    data = await state.get_data()

    if data["service"] == LATINA:
        await state.set_state(Form.days)

        await message.answer(
            "Выберите удобный день для посещения группы:", reply_markup=latina_keyboard
        )

    elif data["service"] == TRANSFER:
        await state.set_state(Form.club_reason)

        await message.answer(
            "Расскажите немного о себе и почему хотите перейти к нам в клуб:",
            reply_markup=menu_keyboard,
        )

    elif data["service"] == CHILDREN:
        await state.set_state(Form.group_days)

        await message.answer(
            "У нас есть две группы, выберите подходящую вам по дням из списка",
            reply_markup=group_keyboard,
        )

    else:
        await state.set_state(Form.days)

        await message.answer(
            "Какие дни вам удобны для занятий?\n\n"
            "Например: Пн, Вт или Будние дни после 18:00",
            reply_markup=menu_keyboard,
        )


@router.message(Form.group_days)
async def get_group_days(message: Message, state: FSMContext):

    await state.update_data(group_days=message.text)

    await state.set_state(Form.wishes)

    await message.answer(
        "Будут ли у вас какие-то пожелания?", reply_markup=menu_keyboard
    )


@router.message(Form.club_reason)
async def get_clud_reason(message: Message, state: FSMContext):

    await state.update_data(club_reason=message.text)

    await state.set_state(Form.wishes)

    await message.answer(
        "Будут ли у вас какие-то особые пожелания?", reply_markup=menu_keyboard
    )


@router.message(Form.days)
async def get_days(message: Message, state: FSMContext):

    data = await state.get_data()

    if data["service"] == LATINA:
        await state.update_data(days=message.text)
        await state.update_data(time="20:00")

        await state.set_state(Form.wishes)

        await message.answer(
            "Будут ли у вас какие-то пожелания?\n\n"
            "Например: хочу отработать связку перед турниром",
            reply_markup=menu_keyboard,
        )

    else:
        await state.update_data(days=message.text)

        await state.set_state(Form.time)

        await message.answer(
            "В какое время вам будет удобно прийти на занятия?\n\nНапример: в 17:00",
            reply_markup=menu_keyboard,
        )


@router.message(Form.time)
async def get_time(message: Message, state: FSMContext):

    await state.update_data(time=message.text)

    await state.set_state(Form.wishes)

    await message.answer(
        "Будут ли у вас какие-то пожелания?\n\n"
        "Например: хочу отработать связку перед турниром",
        reply_markup=menu_keyboard,
    )


@router.message(Form.wishes)
async def get_wishes(message: Message, state: FSMContext):

    await state.update_data(wishes=message.text)

    data = await state.get_data()

    trainer = data.get("trainer", "-")
    group_days = data.get("group.days", "-")
    child_name = data.get("child_name", "-")
    club_reason = data.get("club_reason", "-")
    days = data.get("days", "-")
    time = data.get("time", "-")
    telegram_id = message.from_user.id
    username = message.from_user.username or "Не указан"

    add_application(
        username,
        telegram_id,
        data["service"],
        trainer,
        data["name"],
        child_name,
        data["age"],
        data["experience"],
        data["experience_details"],
        data["phone"],
        club_reason,
        group_days,
        days,
        time,
        data["wishes"],
    )

    if data["service"] == CHILDREN:
        await message.answer(
            f"Спасибо за заявку! Скоро мы с вами свяжемся\n\n"
            f"Направление: {data['service']}\n"
            f"Тренер: {trainer}\n\n"
            f"Имя: {data['name']}\n"
            f"Имя ребенка: {data['child_name']}\n"
            f"Возраст: {data['age']}\n"
            f"Опыт: {data['experience']}\n"
            f"Об опыте: {data['experience_details']}\n"
            f"Телефон: {data['phone']}\n\n"
            f"Подходящая группа: {group_days}\n"
            f"Пожелания: {data['wishes']}\n\n"
        )

        await message.bot.send_message(
            ADMIN_ID,
            f"Новая заявка!\n\n"
            f"Username: @{username}\n"
            f"Telegram ID: {telegram_id}\n\n"
            f"Направление: {data['service']}\n"
            f"Тренер: {trainer}\n\n"
            f"Имя: {data['name']}\n"
            f"Имя ребенка: {data['child_name']}\n"
            f"Возраст: {data['age']}\n"
            f"Опыт: {data['experience']}\n"
            f"Об опыте: {data['experience_details']}\n"
            f"Телефон: {data['phone']}\n\n"
            f"Подходящая группа: {group_days}\n"
            f"Пожелания: {data['wishes']}\n\n",
        )

    elif data["service"] == TRANSFER:
        await message.answer(
            f"Спасибо за заявку! Скоро мы с вами свяжемся\n\n"
            f"Направление: {data['service']}\n"
            f"Тренер: {trainer}\n\n"
            f"Имя: {data['name']}\n"
            f"Возраст: {data['age']}\n"
            f"Опыт: {data['experience']}\n"
            f"Об опыте: {data['experience_details']}\n"
            f"Телефон: {data['phone']}\n\n"
            f"Причина перехода: {data['club_reason']}\n"
            f"Пожелания: {data['wishes']}\n\n"
        )

        await message.bot.send_message(
            ADMIN_ID,
            f"Новая заявка!\n\n"
            f"Username: @{username}\n"
            f"Telegram ID: {telegram_id}\n\n"
            f"Направление: {data['service']}\n"
            f"Тренер: {trainer}\n\n"
            f"Имя: {data['name']}\n"
            f"Возраст: {data['age']}\n"
            f"Опыт: {data['experience']}\n"
            f"Об опыте: {data['experience_details']}\n"
            f"Телефон: {data['phone']}\n\n"
            f"Причина перехода: {data['club_reason']}\n"
            f"Пожелания: {data['wishes']}\n\n",
        )

    else:
        await message.answer(
            f"Спасибо за заявку! Скоро мы с вами свяжемся\n\n"
            f"Направление: {data['service']}\n"
            f"Тренер: {trainer}\n\n"
            f"Имя: {data['name']}\n"
            f"Возраст: {data['age']}\n"
            f"Опыт: {data['experience']}\n"
            f"Об опыте: {data['experience_details']}\n"
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
            f"Тренер: {trainer}\n\n"
            f"Имя: {data['name']}\n"
            f"Возраст: {data['age']}\n"
            f"Опыт: {data['experience']}\n"
            f"Об опыте: {data['experience_details']}\n"
            f"Телефон: {data['phone']}\n\n"
            f"Дни: {data['days']}\n"
            f"Время: {data['time']}\n"
            f"Пожелания: {data['wishes']}\n\n",
        )

    await state.clear()
