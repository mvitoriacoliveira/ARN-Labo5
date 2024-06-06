from bing_image_downloader import downloader

QUERIES = [
    "Canard colvert", "Canard souchet", "Canard chipeau",
    "Canard siffleur", "Canard mandarin", "Canard pilet"
]
OUTPUT_DIR = '/dataset_images_part2'
NB_IMAGES = 5

for query in QUERIES:
    downloader.download(
        query, NB_IMAGES, OUTPUT_DIR,
        adult_filter_off=False, force_replace=False, timeout=15
    )