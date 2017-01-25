#!/usr/bin/python

import os,sys

max_file_size = 300 # EXAMPLE: max_file_size = 300 (kilobytes) 
user = ''           # EXAMPLE: user = 'www-data'
group = ''          # EXAMPLE: group = 'www-data'
permissions = ''    # EXAMPLE: permissions = '644' (in octal nomenclature)

if len(sys.argv) > 1:
    workDir = sys.argv[1]
else:
    workDir = "."

imgs = os.listdir(workDir)

for img in imgs:
    size = os.path.getsize(os.path.join(workDir, img))
    if size > (max_file_size*1024):
        os.system('mogrify -quality 30% ' + img)
        os.system('chmod ' + user + ':' + group + ' ' + img)
        os.system('chmod ' + permissions + img)
