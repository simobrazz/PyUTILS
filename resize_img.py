import argparse
import logging
import os

import PIL
import glob

from PIL import Image

LOG_FORMATTER = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
ROOT_LOGGER = logging.getLogger()
ROOT_LOGGER.setLevel(logging.DEBUG)

FILE_HANDLER = logging.FileHandler("resising_img.log")
FILE_HANDLER.setFormatter(LOG_FORMATTER)
ROOT_LOGGER.addHandler(FILE_HANDLER)

ROOT_LOGGER.info("PyUTILS - resizing img")

parser = argparse.ArgumentParser(description="PyUTILS - resizing img")
parser.add_argument("source_dir", type=str)
parser.add_argument("--destination_dir")

args = parser.parse_args()

imgs = glob.glob(os.path.join(args.source_dir, "*.jpg"))

ROOT_LOGGER.debug("Found %d images.", len(imgs))

dest_dir = os.path.join(os.path.dirname(args.source_dir), os.path.basename(args.source_dir) +
                        "_resized")
if not os.path.exists(dest_dir):
    os.mkdir(dest_dir)

maximum_size = 800

for img in imgs:
    img_obj = Image.open(img)
    exif = img_obj.info['exif']
    if img_obj.width > maximum_size or img_obj.height > maximum_size:
        if img_obj.height > img_obj.width:
            factor = maximum_size / img_obj.height
        else:
            factor = maximum_size / img_obj.width
        size = (int(img_obj.width * factor), int(img_obj.height * factor))
        resized = img_obj.resize(size, PIL.Image.LANCZOS)
        resized.save(os.path.join(dest_dir, os.path.basename(img)), exif=exif)