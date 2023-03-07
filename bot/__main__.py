import asyncio
import os
import logging
from aiogram import Dispatcher, Bot
from commands import register_user_commands


async def main() -> None:
    token = os.getenv('TELEGRAM_TOKEN_API')

    logging.basicConfig(level=logging.DEBUG)

    dispatcher = Dispatcher()
    bot = Bot(token)

    register_user_commands(dispatcher)

    await dispatcher.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except(KeyboardInterrupt, SystemExit):
        print('Bot stopped')
