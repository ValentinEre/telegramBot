import random

from aiogram import types

from bot.model.video import Video


async def start_making(message: types.Message) -> None:
    for x in range(60):
        video = Video()
        video.download_images(video.topic, video.path_to_pic, 12)
        video.resize_pic()
        video.get_clip()
        video.remove_pic()
        await message.answer(f'{x + 1}. {video.topic} was generated')


async def stop_making(message: types.Message) -> None:
    random_num = random.choice(range(2))
    await message.answer(f'{random_num}')
