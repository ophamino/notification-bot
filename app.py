import asyncio

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from data import config

from utils.notify_admins import on_startup_notify
from utils import set_default_commands
from utils.db_api import db_start

from handlers.users import user_router
from handlers.admin import admin_router
from handlers.users.upsheduler import auto_shed


async def on_startup(dispatcher: Dispatcher, bot: Bot) -> None:
    await on_startup_notify(dispatcher, bot)
    await set_default_commands(bot)
    db_start()


async def main() -> None:
    bot = Bot(token=config.BOT_TOKEN, parse_mode="MarkdownV2")
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    dp.startup.register(on_startup)
    dp.include_router(user_router)
    dp.include_router(admin_router)

    auto_shed(bot)
    await on_startup(dp, bot)
    print("Отправил администраторам сообщения.")
    print("Все хендлеры работают.")

    try:
        await dp.start_polling(bot)

    finally:
        await dp.storage.close()
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())
