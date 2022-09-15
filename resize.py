import os
import cv2 as cv

path = "orig_negatives\\"
dir_list = os.listdir(path)

for dir in dir_list:
    img = cv.imread(path+dir)
    img = cv.resize(img, (640, 480), interpolation=cv.INTER_NEAREST)
    cv.imwrite(f"negatives\\{dir}", img)
    print(f"Saved to negatives\\{dir}")