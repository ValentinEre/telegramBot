import glob
import random

from PIL import Image
from icrawler.builtin import GoogleImageCrawler
from moviepy.editor import *
#


class Video:

    def __init__(self):
        key_words = ['Tulips', 'Orchids', 'Lilies', 'Lotus', 'Dahlia flower', 'Apple blossom', 'lily flower',
                     'Snapdragons', 'Aster',
                     'Violet flower', 'Bamboo', 'Gladioli flower', 'Cherry Tree', 'Pine Tree', 'mountain', 'river',
                     'sun']
        self.keyWord = random.choice(key_words)
        self.path_to_pic = '/home/valentin/Изображения/pictures'
        self.path_to_video = '/home/valentin/Видео/videos'
        self.path_to_resize_pic = '/home/valentin/Изображения/pic_1080x1920'
        self.random_num = random.randrange(10000)

    @staticmethod
    def get_random_types():
        types = ['spring', 'deep', 'marvelous', 'wild', 'life-giving', 'indescribable', 'unusual',
                 'autumn', 'landscape', 'norwegian', 'norway', 'france', 'japan', 'snowy', 'sunrise']
        return random.choice(types)

    def new_sentence(self):
        return self.keyWord + ' ' + self.get_random_types()

    def get_pic(self):
        google_crawler = GoogleImageCrawler(
            downloader_threads=4,
            storage={'root_dir': f'{self.path_to_pic}'})
        filters = dict(
            license='commercial,modify')
        google_crawler.crawl(keyword=self.new_sentence(), filters=filters, offset=0, max_num=12, file_idx_offset=0)

    def resize_pic(self):
        print("Now resize")
        images = [f for f in glob.glob(self.path_to_pic + '/*.jpg')]

        pic_num = 0
        for pic in images:
            image = Image.open(f'{pic}')
            new_image = image.resize((1500, 1920))
            new_image.save(f'{self.path_to_resize_pic + "/" + self.new_sentence().replace(" ", "") + str(pic_num)}.jpg')
            pic_num += 1

    def get_clip(self):
        print("Making video")
        directory_for_video = f'{self.path_to_video}'
        directory_with_pic = f'{self.path_to_resize_pic}'
        images = [f for f in glob.glob(directory_with_pic + '/*.jpg')]
        clip = [ImageClip(m).set_duration(5) for m in images]
        final_clip = concatenate_videoclips(clips=clip, method="compose")
        final_clip.write_videofile(
            f'{directory_for_video}/{(self.new_sentence()).replace(" ", "")}_{self.random_num}.WebM', fps=30)

    def remove_pic(self):
        directory_resize = f'{self.path_to_resize_pic}'
        directory = f'{self.path_to_pic}'
        for f in os.listdir(directory):
            os.remove(os.path.join(directory, f))
        for f in os.listdir(directory_resize):
            os.remove(os.path.join(directory_resize, f))
        print("Cleaning is over")


v = Video()
v.get_pic()
v.resize_pic()
v.get_clip()
v.remove_pic()
