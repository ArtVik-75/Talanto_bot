from aiogram.fsm.state import State, StatesGroup

class Form(StatesGroup):
    service = State()
    trainer = State()
    group = State()

    name = State()
    child_name = State()
    age = State()
    
    group_days = State()
    club_reason = State()
    experience = State()
    experience_details = State()

    phone = State()

    days = State()
    time = State()

    wishes = State()