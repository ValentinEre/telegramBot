from unittest.mock import AsyncMock
import pytest
from aiogram.types import KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from bot.commands.start import start_bot


@pytest.mark.asyncio
async def test_start_hand():
    message = AsyncMock()
    await start_bot(message=message)
    menu_builder = ReplyKeyboardBuilder()
    menu_builder.add(
        KeyboardButton(text='/StartBot▶️'),
        KeyboardButton(text='/StopBot🛑')
    )
    message.answer.assert_called_with(
        'Menu',
        reply_markup=menu_builder.as_markup(resize_keyboard=True)
    )
