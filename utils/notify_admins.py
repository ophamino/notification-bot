import logging

from datetime import datetime
from aiogram import Bot, Dispatcher

from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher, bot: Bot):
    me = await bot.get_me()

    for admin in ADMINS:
        try:

            await bot.send_message(admin,
                  f'Запущен бот\n\n'
                  f'Информация о боте:\nИмя: {me.full_name}\n'
                  f'Айди: {me.id}')

        except Exception as err:
            logging.exception(err)
