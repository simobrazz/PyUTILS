import os
import glob
import argparse
import shutil
from zipfile import ZipFile

parser = argparse.ArgumentParser("Unzip files")
parser.add_argument("root_dir", help="rootdir to scan")
parser.add_argument("--group_zip_files", help="If grouping zip files", default=0, type=int)

args = parser.parse_args()

root_dir = args.root_dir
group_zip_files = args.group_zip_files

zip_files = glob.glob(os.path.join(root_dir, "*.zip"))

for fn in zip_files:
    with ZipFile(fn) as current_zip:
        basename = os.path.basename(fn).split(".")[0]
        current_zip.extractall(os.path.join(root_dir, basename))

if group_zip_files:
    archive_folder = os.path.join(root_dir, "Archives")
    if not os.path.exists(archive_folder):
        os.mkdir(archive_folder)
    for zip_file in zip_files:
        shutil.move(zip_file, archive_folder)
