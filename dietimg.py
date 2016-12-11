#!/usr/bin/python3.5

import os,sys

MAX_FILE_SIZE = 300

if len(sys.argv) > 1:
    workDir = sys.argv[1]
else:
    workDir = "."

imgs = os.listdir(workDir)

for img in imgs:
    size = os.path.getsize(os.path.join(workDir, img))
    if size > (MAX_FILE_SIZE*1024):
        print("{0} is {1} bytes.".format(img, size))
