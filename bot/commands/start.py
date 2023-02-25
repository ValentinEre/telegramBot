from aiogram import types
from aiogram.utils.keyboard import (ReplyKeyboardBuilder, KeyboardButton)


async def start_bot(message: types.Message) -> None:
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.add(
        KeyboardButton(text='/StartBot▶️'),
        KeyboardButton(text='/StopBot🛑')
    )

    await message.answer(
        'Menu',
        reply_markup=menu_builder.as_markup()
    )
