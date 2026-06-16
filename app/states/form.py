from aiogram.fsm.state import State, StatesGroup


class Form(StatesGroup):
    service = State()
    trainer = State()

    name = State()
    age = State()
    phone = State()

    days = State()
    time = State()

    wishes = State()
