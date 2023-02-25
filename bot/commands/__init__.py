__all__ = ['register_user_commands']

from aiogram import Router
from aiogram.filters import CommandStart, Command

from bot.commands.functional import start_making, stop_making
from bot.commands.start import start_bot


def register_user_commands(router: Router) -> None:
    router.message.register(start_bot, CommandStart())
    router.message.register(start_making, Command(commands=['StartBot▶️']))
    router.message.register(stop_making, Command(commands=['StopBot🛑']))
