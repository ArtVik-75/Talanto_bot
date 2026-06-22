from aiogram.fsm.state import State, StatesGroup

class AdminForm(StatesGroup):
    application_number = State()