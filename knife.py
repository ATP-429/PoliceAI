import cv2 as cv

hand_cascade = cv.CascadeClassifier('cascade.xml')

vid = cv.VideoCapture(0)

while True:
    ret, img = vid.read()
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    hands = hand_cascade.detectMultiScale(img, 1.3, 5)

    for (x, y, w, h) in hands:
        print("Knife detected")
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    cv.imshow('Knives', img)
    cv.waitKey(1)