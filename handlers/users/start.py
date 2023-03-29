from random import choice

from aiogram import Router, Bot
from aiogram.types import Message
from aiogram.filters import Command

from utils.db_api import db_timetable, db_photo
from utils.extends import msg, sender, check_user


user_router = Router()


@user_router.message(Command(commands=['start', 'help']))
async def start_bot(message: Message) -> None:
    await check_user(message)
    await message.answer(
        '*Привет\!*, я бот 5 группы 1 курса ЭФ\n'
        '*Мои команды:*\n\n'
        '/today \- *Отправить сегодняшнее расписание*\n'
        '/tomorrow \- *Отправить завтрашнее расписание*\n'
        '/photo \- *Отправить рандомное фото, мем*\n'
        '/info \- *Информация о боте и его владельце*\n\n')


@user_router.message(Command(commands=['today']))
async def today(message: Message, bot: Bot) -> None:
    numday: int = db_timetable.get_day()[0]
    if numday not in (6, 7, 13, 14):
        try:
            await message.answer(msg(numday))
        except TypeError:
            await sender(bot, msg, numday)
    else:
        await message.answer("Сегодня выходной, отдыхайте, родные")


@user_router.message(Command(commands=['tomorrow']))
async def tomorrow(message: Message, bot: Bot) -> None:
    numday: int = db_timetable.get_day()[0]
    if numday not in (5, 6, 12, 13):
        try:
            await message.answer(msg(numday + 1))
        except TypeError:
            await sender(bot, msg, numday + 1)
    else:
        await message.answer("Завтра выходной, отдыхайте, пуспики")


@user_router.message(Command(commands=['photo']))
async def send_random_photo(message: Message) -> None:
    try:
        photo_id = choice(db_photo.get_photo())[0]
        await message.answer_photo(photo=photo_id)
    except IndexError:
        await message.answer("Нет фотографий")


@user_router.message(Command(commands=['admin_panel']))
async def admin_panel(message: Message) -> None:
    await message.answer("*Команды для администраторов:*\n\n"
                         "/notification \- _ отправить уведомление всем участникам _\n"
                         "/add\_photo \-  _ добавить фото в коллаж _")


@user_router.message(Command(commands=['info']))
async def send_schedule(message: Message) -> None:
    await message.answer(
        "*Автор бота:* Алисултанов Джамалудин\n"
        "*Telegram:* @vocao\n\n"
        "*Будущие обновления:*\n"
        '\[ \+ \]    _ Локальная фраза кого\-то из участников _\n'
        '\[ \+ \]    _ Система уведомления участников о паре\
        и номере кабинета на каждой перемене _')
