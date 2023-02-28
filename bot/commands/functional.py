import sys

from aiogram import types
import os
from bot.model.video import Video


async def start_making(message: types.Message) -> None:
    range_of_10 = range(10)
    for x in range_of_10:
        video = Video()
        video.get_pic()
        #video.get_clip()
        video.remove_pic()
        await message.answer(f'{x}. Was generated {video.new_sentence()}')


async def stop_making(message: types.Message) -> None:
    await message.answer('Stop_making')
