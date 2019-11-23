#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 18:41:54 2019

@author: simonebrazzo
"""

from os import path
import glob
import os

from shutil import copyfile

src = "/Users/simonebrazzo/Desktop/Pictures/Photos"
dst = "/Volumes/SEAGATE EXP/Simone/Photos"

src_files = glob.glob(path.join(src, "**", "*"), recursive=True)

file_transfer = open("./file_transfer.log", "w")

for index, src_file in enumerate(src_files):
    print("%d/%d" % (index, len(src_files)))
    if path.isdir(src_file):
        current_dest = path.join(dst, path.relpath(src_file, src))
        if not path.exists(current_dest):
            print("Creating directory:" + current_dest)
            file_transfer.write("Writing directory %s \n" % current_dest)
            os.mkdir(current_dest)
        else:
            print("Directory already exists:" + current_dest)
            file_transfer.write("Directory already exists %s \n" % current_dest)
    elif path.isfile(src_file):
        current_dest = path.join(dst, path.relpath(src_file, src))
        if not path.exists(current_dest):
            print("Creating file:" + current_dest)
            file_transfer.write("Writing file %s \n" % current_dest)
            copyfile(src_file, current_dest)
        else:
            print("File already exists:" + current_dest)
            file_transfer.write("File already exists %s \n" % current_dest)
    else:
        print("Unknown file type")
        file_transfer.write("Unknown file type %s \n" % current_dest)
            

file_transfer.close()