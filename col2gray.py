import os
import cv2 as cv
import time

path = "hands2\\"
dir_list = os.listdir(path)

for dir in dir_list:
    img = cv.imread(path+dir)
    filename = dir[:-4:]  # Remove the '.png' characters (last 4 chars) from the end
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite(f"negatives\\{filename}.jpg", img)
