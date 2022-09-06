from screen import screen_grab

import cv2 as cv
import numpy as np

import win32gui, win32con, win32api


def getWindowHandle(win_name):
    return win32gui.FindWindowEx(None, None, None, win_name)

def setClickthrough(win_name):
    hwnd = getWindowHandle(win_name)
    try:
        l_ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        l_ex_style |= win32con.WS_EX_TRANSPARENT | win32con.WS_EX_LAYERED
        l_ex_style &= ~(win32con.WS_EX_DLGMODALFRAME | win32con.WS_EX_CLIENTEDGE | win32con.WS_EX_STATICEDGE)
        win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, l_ex_style)

        l_style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
        l_style &= ~(win32con.WS_CAPTION | win32con.WS_THICKFRAME | win32con.WS_MINIMIZEBOX | win32con.WS_MAXIMIZEBOX | win32con.WS_SYSMENU)
        win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, l_style)

        win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(0,0,0), 100, win32con.LWA_ALPHA)
    except Exception as e:
        print(e)

cascade = cv.CascadeClassifier('cascade2.xml')

#vid = cv.VideoCapture(0)

WIDTH, HEIGHT = 1920, 1080
SCALE = 1

overlay = np.zeros((HEIGHT//SCALE, WIDTH//SCALE, 3), np.uint8)
cv.imshow('Overlay', overlay)
cv.moveWindow('Overlay', 0, 0)
cv.setWindowProperty('Overlay', cv.WND_PROP_TOPMOST, 1)
setClickthrough('Overlay')

while True:
    #ret, img = vid.read()
    img = cv.imread('test.jpg')
    # img = screen_grab('firefox')
    # img = cv.resize(img, (WIDTH//SCALE, HEIGHT//SCALE), interpolation=cv.INTER_LINEAR)

    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    overlay = np.zeros((HEIGHT//SCALE, WIDTH//SCALE, 3), np.uint8)

    knives = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=400, minSize=(100, 100), maxSize=(400, 400))

    for (x, y, w, h) in knives:
        print("Knife detected")
        cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    
    overlay = cv.resize(overlay, (WIDTH, HEIGHT), interpolation=cv.INTER_NEAREST)
    cv.imshow('Overlay', img)
    cv.waitKey(1)