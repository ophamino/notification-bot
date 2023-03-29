from aiogram.fsm.state import State, StatesGroup


class PhotoSG(StatesGroup):
    get_photo = State()
    confirm = State()
