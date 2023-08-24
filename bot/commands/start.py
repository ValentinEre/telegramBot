from aiogram import types
from aiogram.utils.keyboard import (ReplyKeyboardBuilder, KeyboardButton)


async def start_bot(message: types.Message):
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.add(
        KeyboardButton(text='/StartBot▶️'),
        KeyboardButton(text='/IsAlive🧐')
    )

    return await message.answer(
        'Menu',
        reply_markup=menu_builder.as_markup(resize_keyboard=True)
    )
