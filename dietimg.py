#!/usr/bin/python

import os,sys

MAX_FILE_SIZE = 300 # EXAMPLE: MAX_FILE_SIZE = 300 (kilobytes) 
user = 'www-data'           # EXAMPLE: user = 'www-data'
group = 'www-data'          # EXAMPLE: group = 'www-data'
permissions = '664'    # EXAMPLE: permissions = '644' (in octal nomenclature)
quality = '30%'

if len(sys.argv) > 1:
    workDir = sys.argv[1]
else:
    workDir = "."

imgs = os.listdir(workDir)

for img in imgs:
    size = os.path.getsize(os.path.join(workDir, img))
    if size > (MAX_FILE_SIZE*1024):
        os.system('mogrify -quality '+ quality +' ' + img)
	os.system('chown '+ user +':'+ group +' ' + img)
	os.system('chmod '+ permissions +' ' + img)

