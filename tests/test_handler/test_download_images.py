import os
import pytest
from icrawler.builtin import GoogleImageCrawler


@pytest.mark.asyncio
def test_download_images():
    # Define search query and number of images to download
    query = "dogs"
    num_images = 3

    # Download images using icrawler
    output_dir = "../test_images"
    crawler = GoogleImageCrawler(storage={"root_dir": output_dir})
    crawler.crawl(keyword=query, max_num=num_images)

    # Verify that at least one image was downloaded successfully
    images = os.listdir(output_dir)
    assert len(images) > 0

    # Clean up test artifacts
    for image in images:
        os.remove(os.path.join(output_dir, image))
