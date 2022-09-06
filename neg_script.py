import os
import imagesize

path = "negatives\\"
dir_list = os.listdir(path)

f = open('negatives.txt', 'w')
for dir in dir_list:
    width, height = imagesize.get(path+dir)
    if width > 300 and height > 300:
        f.write(path+dir+'\n')
    