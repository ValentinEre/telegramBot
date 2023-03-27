import glob
import random

from PIL import Image
from icrawler.builtin import GoogleImageCrawler
from moviepy.editor import *


class Video:

    def __init__(self):

        # Список игр и тем
        games = {
            "Minecraft": [
                "Локации и карты",
                "Строительство и дизайн",
                "Создание и прокачка персонажей",
                "Мобы и животные",
                "Крафтинг и ресурсы",
                "Фан-арт и косплей"
            ],
            "Fortnite": [
                "Скины и косметические предметы",
                "Локации и карты",
                "Оружие и снаряжение",
                "Персонажи и их способности",
                "События и праздники, связанные с игрой",
                "Награды и достижения в игре"
            ],
            "PUBG": [
                "Локации и карты",
                "Оружие и снаряжение",
                "Персонажи и их способности",
                "Награды и достижения в игре",
                "Квесты и миссии",
                "Фан-арт и косплей"
            ],
            "Call of Duty: Mobile": [
                "Локации и карты",
                "Оружие и снаряжение",
                "Персонажи и их способности",
                "Награды и достижения в игре",
                "Квесты и миссии",
                "События и праздники, связанные с игрой"
            ],
            "Clash of Clans": [
                "Строительство и дизайн",
                "Создание и прокачка персонажей",
                "Награды и достижения в игре",
                "Квесты и миссии",
                "События и праздники, связанные с игрой",
                "Фан-арт и косплей"
            ],
            "Among Us": [
                "Персонажи и их способности",
                "Локации и карты",
                "Фан-арт и косплей",
                "События и праздники, связанные с игрой",
                "Награды и достижения в игре",
                "Моды и дополнения"
            ],
            "Roblox": [
                "Создание и прокачка персонажей",
                "Локации и карты",
                "Мини-игры и развлечения",
                "События и праздники, связанные с игрой",
                "Награды и достижения в игре",
                "Фан-арт и косплей"
            ]
        }

        game = random.choice(list(games.keys()))
        theme = random.choice(games[game])

        self.game_theme = f"${game}_{theme}"
        self.topic = f"${game} {theme}"

        self.path_to_pic = "/home/valentin/Изображения/pictures"
        self.path_to_video = "/home/valentin/Видео/vid"
        self.path_to_audio = "/home/valentin/Музыка/music"
        self.path_to_resize_pic = "/home/valentin/Изображения/pic_1080x1920"
        self.random_num = random.randrange(77777)

    def get_pic(self):
        google_crawler = GoogleImageCrawler(
            downloader_threads=2,
            storage={"root_dir": f"{self.path_to_pic}"})
        filters = dict(
            type="photo",
            license="commercial,modify"
        )
        google_crawler.crawl(self.topic, filters=filters, offset=0, max_num=12, file_idx_offset=0)

    def resize_pic(self):
        print("Now resize")
        images = [f for f in glob.glob(self.path_to_pic + "/*.jpg")]

        pic_num = 0
        for pic in images:
            image = Image.open(f"{pic}")
            new_image = image.resize((1600, 1920))
            new_image.save(f'{self.path_to_resize_pic + "/" + self.game_theme + str(pic_num)}.jpg')
            pic_num += 1

    def get_clip(self):
        print("Making video")
        dir_for_video = f"{self.path_to_video}"
        dir_with_pic = f"{self.path_to_resize_pic}"
        dir_with_audio = self.path_to_audio
        audio = [f for f in glob.glob(dir_with_audio + "/*.mp3")]
        images = [f for f in glob.glob(dir_with_pic + "/*.jpg")]
        if len(images) != 0:
            clip = [ImageClip(m).set_duration(2) for m in images]
            audio_file = (AudioFileClip(random.choice(audio))) \
                .subclip(0, 24).audio_fadein(1).audio_fadeout(1).volumex(0.3)
            final_clip = concatenate_videoclips(clips=clip, method="compose") \
                .fadein(1).fadeout(1).set_audio(audio_file)
            final_clip.write_videofile(
                f"{dir_for_video}/{self.game_theme}_{self.random_num}.mp4", fps=30)

    def remove_pic(self):
        dir_pic_default = f"{self.path_to_pic}"
        dir_pic_resize = f"{self.path_to_resize_pic}"
        for f in os.listdir(dir_pic_default):
            os.remove(os.path.join(dir_pic_default, f))
        for f in os.listdir(dir_pic_resize):
            os.remove(os.path.join(dir_pic_resize, f))
        print("Cleaning is over")
