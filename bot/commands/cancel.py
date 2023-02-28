from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def cancel_board() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder
    builder.button('Cancel')
    return builder.as_markup(resize_keyboard=True)
