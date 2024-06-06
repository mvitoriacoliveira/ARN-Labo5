from bing_image_downloader import downloader

QUERIES = [
    "Chess King", "Chess Queen", "Chess Rook",
    "Chess Bishop", "Chess Knight", "Chess Pawn"
]
OUTPUT_DIR_BASE = '/dataset_images_part2'
NB_IMAGES = 50

for query in QUERIES:
    downloader.download(
        query, limit = NB_IMAGES,  output_dir=OUTPUT_DIR_BASE,
        adult_filter_off=False, force_replace=False, timeout=15
    )