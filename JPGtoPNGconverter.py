# run with two args, first is foldername/ newfoldertocreate/

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
    f = os.path.join(origin_folder, filename)

    if os.path.isfile(f):
        print(f)
        img = Image.open(f)
        img.save(f, 'png')
