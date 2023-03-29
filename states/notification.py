from aiogram.fsm.state import State, StatesGroup


class NotificationSG(StatesGroup):
    get_message = State()
    confirm = State()
