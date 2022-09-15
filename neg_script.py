import os

path = "negatives\\"
dir_list = os.listdir(path)

f = open('negatives.txt', 'w')
for dir in dir_list:
    f.write(path+dir+'\n')
    