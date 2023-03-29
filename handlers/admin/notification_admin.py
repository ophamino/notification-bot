import asyncio

from aiogram import Router, Bot, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from states import NotificationSG
from keyboards.inline import confirm_ikeyboard
from utils.db_api import db_users
from data.config import ADMINS


notication_router = Router()


@notication_router.message(Command(commands=['notification']))
async def sender(message: Message, state: FSMContext):
    if not message.from_user:
        return
    if message.from_user.id in ADMINS:
        await message.answer("Отправьте сообщение, которое нужно разослать")
        await state.set_state(NotificationSG.get_message)
    else:
        await message.answer("Эта команда только для администраторов")


@notication_router.message(NotificationSG.get_message)
async def get_message(message: Message, state: FSMContext):
    await message.answer(
        f"*Сообщение которое вы хотите отправить выглядит так:*\n\n"
        f"{message.text}"
        f'\n\n*Нажмите кнопку для подтверждения*',
        reply_markup=confirm_ikeyboard())
    await state.update_data(message_text=message.text)
    await state.set_state(NotificationSG.confirm)


@notication_router.callback_query(NotificationSG.confirm)
async def sender_decide(call: CallbackQuery, bot: Bot, state: FSMContext):
    data = await state.get_data()
    message_text = data.get('message_text')
    if not call.message:
        return
    if call.data == "yes":
        await call.message.edit_text("Начинаю рассылку\.")
        for user in db_users.get_all_users():
            try:
                await bot.send_message(int(user[0]), f"‼️‼️‼️*Уведомление*\n\n{message_text}")
                await asyncio.sleep(0.1)
            except Exception:
                continue
        await call.message.edit_text("Успешно разослано")

    if call.data == "no":
        await call.message.edit_text("Отменил рассылку")
    await state.clear()
