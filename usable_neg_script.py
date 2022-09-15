import os
import imagesize

path = "negatives\\"
dir_list = os.listdir(path)

f = open('usable_negatives.txt', 'w')
for dir in dir_list:
    width, height = imagesize.get(path+dir)
    if width >= 400 and height >= 400:
        f.write(path+dir+'\n')