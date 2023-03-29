import asyncio
from typing import Callable

from aiogram import Bot
from aiogram.types import Message

from ..db_api import db_lessons, db_timetable, db_users


def number_of_week() -> int:
    num_day: int = db_timetable.get_day()[0]
    weekday: int = db_timetable.get_weekday(num_day)[0]
    if weekday in (14, 1, 2, 3, 4, 5):
        return 1
    return 2


def msg(num_day: int) -> str:
    weekday: int = db_timetable.get_weekday(num_day)[0]
    shedule: list = db_lessons.get_shedule(weekday)

    msg: str = f"*Расписание на {number_of_week()} неделю"\
               f"\- {db_timetable.get_weekday(weekday)[1]}*\n\n"
    for row in shedule:
        msg = msg + f"*{row[1]} пара \- {row[2]}, {row[3]}*\n"\
                    f"*Кабинет:* {row[6]}\nВремя: _{row[4]}\-{row[5]}_\n\n"

    return msg


async def sender(bot: Bot, msg: Callable[[int], str], numday: int) -> None:
    for user in db_users.get_all_users():
        try:
            await bot.send_message(user[0], msg(numday))
            await asyncio.sleep(0.1)
        except Exception:
            continue


async def check_user(message: Message) -> None:
    if not message.from_user:
        return
    if not db_users.user_exists(message.from_user.id):
        db_users.add_user(message.from_user.id,
                          message.from_user.username,
                          message.from_user.full_name)
