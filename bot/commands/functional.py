from aiogram import types


async def start_making(message: types.Message) -> None:
    await message.answer('start_making')


async def stop_making(message: types.Message) -> None:
    await message.answer('stop_making')
