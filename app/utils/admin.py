from aiogram.types import Message

from app.keyboards.pages import applications_pages_keyboard

async def show_applications_page(message: Message, applications, page):

    start = page * 10 
    end = start + 10

    page_applications = applications[start:end]

    text = f"📋 Заявки (страница {page + 1})\n\n"

    if not page_applications:
        return await message.answer(
            "На этой странице нет заявок"
        )

    for number, application in enumerate(
        page_applications,
        start=page * 10 + 1
    ):
        text += (
            f"{number}. {application['Имя']} | "
            f"{application['Услуга']} | "
            f"{application['Дата']}\n"
        )

    await message.answer(text, reply_markup=applications_pages_keyboard)