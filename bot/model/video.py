import glob
import random

from PIL import Image
from icrawler.builtin import GoogleImageCrawler
from moviepy.editor import *


class Video:

    def __init__(self):
        key_words = ['Tulipsflowers', 'Orchidsflowers', 'Liliesflowers', 'Lotusflower', 'Dahliaflower',
                     'Appleblossom', 'lilyflower', 'Snapdragonsflowers', 'Asterflower', 'Violetflower',
                     'Waterfall',
                     'Gladioliflower', 'CherryTree',
                     'PineTree', 'Mountain', 'River', 'Sun']
        self.keyWord = random.choice(key_words)
        self.path_to_pic = '/home/valentin/Изображения/pictures'
        self.path_to_video = '/home/valentin/Видео/vid'
        self.path_to_audio = '/home/valentin/Музыка/music'
        self.path_to_resize_pic = '/home/valentin/Изображения/pic_1080x1920'
        self.random_num = random.randrange(10000)

    @staticmethod
    def get_random_types():
        types = ['spring', 'summer', 'marvelous', 'winter', 'sunset', 'indescribable', 'unusual', 'austria',
                 'autumn', 'landscape', 'norwegian', 'norway', 'france', 'japan', 'snowy', 'sunrise']
        return random.choice(types)

    def new_sentence(self):
        return self.keyWord + ' ' + self.get_random_types()

    def get_pic(self):
        google_crawler = GoogleImageCrawler(
            downloader_threads=2,
            storage={'root_dir': f'{self.path_to_pic}'})
        filters = dict(
            type='photo',
            license='commercial,modify'
        )
        google_crawler.crawl(keyword=self.new_sentence(), filters=filters, offset=0, max_num=12, file_idx_offset=0)

    def resize_pic(self):
        print("Now resize")
        images = [f for f in glob.glob(self.path_to_pic + '/*.jpg')]

        pic_num = 0
        for pic in images:
            image = Image.open(f'{pic}')
            new_image = image.resize((1600, 1920))
            new_image.save(f'{self.path_to_resize_pic + "/" + self.keyWord + str(pic_num)}.jpg')
            pic_num += 1

    def get_clip(self):
        print("Making video")
        dir_for_video = f'{self.path_to_video}'
        dir_with_pic = f'{self.path_to_resize_pic}'
        dir_with_audio = self.path_to_audio
        audio = [f for f in glob.glob(dir_with_audio + "/*.mp3")]
        images = [f for f in glob.glob(dir_with_pic + '/*.jpg')]
        if len(images) != 0:
            clip = [ImageClip(m).set_duration(2) for m in images]
            audio_file = (AudioFileClip(random.choice(audio))) \
                .subclip(0, 24).audio_fadein(1).audio_fadeout(1).volumex(0.3)
            final_clip = concatenate_videoclips(clips=clip, method="compose") \
                .fadein(1).fadeout(1).set_audio(audio_file)
            final_clip.write_videofile(
                f'{dir_for_video}/{self.keyWord}_{self.random_num}.mp4', fps=30)

    def remove_pic(self):
        dir_pic_default = f'{self.path_to_pic}'
        dir_pic_resize = f'{self.path_to_resize_pic}'
        for f in os.listdir(dir_pic_default):
            os.remove(os.path.join(dir_pic_default, f))
        for f in os.listdir(dir_pic_resize):
            os.remove(os.path.join(dir_pic_resize, f))
        print("Cleaning is over")
