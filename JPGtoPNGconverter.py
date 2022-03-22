from distutils.command.clean import clean
import sys
import os
from os import path
from PIL import Image

# use sys to grab first and second args
# sys.argv[1] sys.argv[2]
origin_folder = sys.argv[1]
target_folder = sys.argv[2]

# check is new folder/exists, if not create

if not os.path.exists(target_folder):
    os.mkdir(target_folder)
else:
    print('already exist. pass')

# loop through origin, grab each, convert to png, store on new folder

for filename in os.listdir(origin_folder):
    img = Image.open(f'{origin_folder}{filename}')

    # necesitamos remover la ext .jpg, devuelve tupple. 0 es filename
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{target_folder}{clean_name}.png', 'png')
    print('all done')
