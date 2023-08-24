import glob
import hashlib
import random

from PIL import Image
from icrawler.builtin import BingImageCrawler
from moviepy.editor import *


class Video:

    def __init__(self):

        # Список игр и тем
        games = {
            "Minecraft": [
                "Landscapes",
                "Building creations",
                "Mobs and creatures",
                "Fan art and cosplay"
            ],
            "Fortnite": [
                "Skins and cosmetics",
                "Locations on the map",
                "Weapons and equipment"
            ],
            "PUBG": [
                "Locations on the map",
                "Weapons and equipment",
                "Fan art and cosplay"
            ],
            "Call of Duty: Mobile": [
                "Locations and maps",
                "Weapons and equipment",
                "Rewards and achievements in the game",
                "Quests and missions"
            ],
            "Clash of Clans": [
                "Rewards and achievements in the game",
                "Fan art and cosplay"
            ],
            "Apex Legends": [
                "Legends",
                "Locations",
                "Fan art and cosplay",
                "Game events and holidays",
                "Fan art and cosplay"
            ],
            "Roblox": [
                "Character creation and leveling up",
                "Locations and maps",
                "Mini-games and entertainment",
                "Fan art and cosplay"
            ],
            "League of Legends": [
                "Champions ",
                "Locations",
                "Fan art and cosplay",
            ]
        }

        self.game = random.choice(list(games.keys()))
        theme = random.choice(games[self.game])

        self.game_theme = f"${self.game}_{theme}"
        self.topic = f"${self.game} mobile {theme}"

        self.path_to_pic = "/home/valentin/Pictures/pictures"
        self.path_to_video = "/home/valentin/Videos/video"
        self.path_to_audio = "/home/valentin/Music/music"
        self.path_to_resize_pic = "/home/valentin/Pictures/pic_1080x1920"
        self.random_num = random.randrange(77777)

    def download_images(self, keyword, save_dir, num_images):
        image_hashes = set()
        num_downloaded = 0
        while num_downloaded < num_images:
            crawler = BingImageCrawler(storage={"root_dir": save_dir})
            crawler.crawl(keyword=keyword, max_num=num_images, min_size=(400, 400))
            for root, _, files in os.walk(save_dir):
                for file in files:
                    filepath = os.path.join(root, file)
                    with open(filepath, "rb") as f:
                        image = f.read()
                    image_hash = hashlib.md5(image).hexdigest()
                    if image_hash in image_hashes:
                        os.remove(filepath)
                    else:
                        image_hashes.add(image_hash)
                        num_downloaded += 1
                    if num_downloaded >= num_images:
                        break
                if num_downloaded >= num_images:
                    break

    def resize_pic(self):
        print("Now resizing images")
        images = [f for f in glob.glob(f"{self.path_to_pic}/*.jpg")]
        resized_images = [Image.open(f).resize((1500, 1800)) for f in images]
        for i, img in enumerate(resized_images):
            img.save(f"{self.path_to_resize_pic}/name_{i}.jpg")

    def get_clip(self):
        print("Making video")
        audio_files = [f for f in os.listdir(self.path_to_audio)]
        audio_file = AudioFileClip(f"{self.path_to_audio}/{random.choice(audio_files)}") \
            .subclip(0, 24).audio_fadein(1).audio_fadeout(1).volumex(0.3)
        images = [f for f in os.listdir(self.path_to_resize_pic)]
        clips = [ImageClip(f"{self.path_to_resize_pic}/{f}").set_duration(2) for f in images]
        final_clip = concatenate_videoclips(clips=clips, method="compose") \
            .fadein(1).fadeout(1).set_audio(audio_file)
        final_clip.write_videofile(f"{self.path_to_video}/{self.game}_{self.random_num}.mp4", fps=30)

    def remove_pic(self):
        print("Cleaning up")
        for folder in (self.path_to_pic, self.path_to_resize_pic):
            [os.remove(os.path.join(folder, f)) for f in os.listdir(folder)]
        print("Cleaning done")

