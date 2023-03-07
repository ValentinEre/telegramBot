from aiogram import types

from bot.model.video import Video


async def start_making(message: types.Message) -> None:
    range_of_10 = range(10)
    for x in range_of_10:
        video = Video()
        video.get_pic()
        video.resize_pic()
        video.get_clip()
        video.remove_pic()
        await message.answer(f'{x+1}. {video.keyWord} was generated')


async def stop_making(message: types.Message) -> None:
    await message.answer('Stop_making')
