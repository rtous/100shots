
import json
from os import listdir
from os.path import isfile, join, splitext
import traceback
from shutil import copyfile


#INPUTPATH = "/Volumes/ElementsDat/pose/H36M/ECCV2018/ECCV18_Challenge/Val/IMG"
INPUTPATH = "/Volumes/ElementsDat/pose/COCO/train2017"
OUTPUTPATH = "allImages"

files = [f for f in listdir(INPUTPATH) if isfile(join(INPUTPATH, f))]

i = 0

for filename in files:
	copyfile(join(INPUTPATH, filename), join(OUTPUTPATH, filename))
	i += 1
	if i == 1000:
		break


	