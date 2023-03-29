import asyncio

from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states import PhotoSG
from keyboards.inline import confirm_ikeyboard
from utils.db_api import db_photo
from data.config import ADMINS


photo_router = Router()


@photo_router.message(Command(commands=['add_photo']))
async def sender(message: Message, state: FSMContext):
    if not message.from_user:
        return
    if message.from_user.id in ADMINS:
        await message.answer("Отправьте фото, которое нужно добавить")
        await state.set_state(PhotoSG.get_photo)
    else:
        await message.answer("Эта команда только для администраторов")


@photo_router.message(PhotoSG.get_photo, F.photo)
async def get_message(message: Message, state: FSMContext):
    await message.answer_photo(message.photo[-1].file_id)
    await message.answer('*Нажмите кнопку для подтверждения*',
                         reply_markup=confirm_ikeyboard())
    await state.update_data(file_id=message.photo[-1].file_id)
    await state.set_state(PhotoSG.confirm)


@photo_router.callback_query(PhotoSG.confirm)
async def sender_decide(call: CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    file_id = data.get('file_id')
    if not call.message:
        return
    if call.data == "yes":
        db_photo.add_photo(file_id)
        await call.message.edit_text("Успешно добавлено")
    if call.data == "no":
        await call.message.edit_text("Отменил добавление")
    await state.clear()
