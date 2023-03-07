import os
import pytest
from icrawler.builtin import GoogleImageCrawler


@pytest.mark.asyncio
def test_download_images():
    query = "dogs"
    num_images = 3

    output_dir = "/test_images"
    crawler = GoogleImageCrawler(storage={"root_dir": output_dir})
    crawler.crawl(keyword=query, max_num=num_images)

    images = os.listdir(output_dir)
    assert len(images) > 0

    for image in images:
        os.remove(os.path.join(output_dir, image))
