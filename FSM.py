from aiogram.fsm.state import StatesGroup, State


class step_message(StatesGroup):
    message = State()