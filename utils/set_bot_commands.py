from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_default_commands(bot: Bot) -> None:
    commands = [
        BotCommand(
            command='start',
            description='Запустить бота'
        ),
        BotCommand(
            command='today',
            description='Расписание на сегодня'
        ),
        BotCommand(
            command='tomorrow',
            description='Расписание на завтра'
        ),
        BotCommand(
            command="photo",
            description="Прислать рандомное фото"
        ),
        BotCommand(
            command="admin_panel",
            description="Административная панель"
        ),
        BotCommand(
            command='info',
            description='Инфо о боте'
        )
    ]

    await bot.set_my_commands(commands, BotCommandScopeDefault(type='default'))
