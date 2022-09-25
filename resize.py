import os
import cv2 as cv

path = "new_negatives\\"
dir_list = os.listdir(path)

for dir in dir_list:
    try:
        img = cv.imread(path+dir)
        img = cv.resize(img, (480, 270), interpolation=cv.INTER_LINEAR)
        img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        cv.imwrite(f"negatives\\{dir}", img)
        print(f"Saved to negatives\\{dir}")
    except:
        print(f"Failed to save {path+dir}")