from aiogram.types import Message
from aiogram import Bot

from apscheduler.schedulers.asyncio import AsyncIOScheduler

from .start import today, tomorrow
from utils.db_api import db_timetable


def auto_shed(bot: Bot, *args, **kwargs) -> None:
    sheduler = AsyncIOScheduler(timezone='Europe/Moscow')

    sheduler.add_job(tomorrow,
                     trigger='cron',
                     hour=18,
                     minute=0,
                     kwargs={'bot': bot, "message": Message})
    sheduler.add_job(today,
                     trigger='cron',
                     hour=7,
                     minute=00,
                     kwargs={'bot': bot, "message": Message})
    sheduler.add_job(db_timetable.next_day,
                     trigger='cron',
                     hour=00,
                     minute=00)

    sheduler.start()
