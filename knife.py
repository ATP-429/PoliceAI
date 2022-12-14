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

cascade = cv.CascadeClassifier('cascade9.xml')

vid = cv.VideoCapture(0)

WIDTH, HEIGHT = 1920, 1080
REDUCED_WIDTH , REDUCED_HEIGHT = 1920//4, 1080//4

overlay = np.zeros((REDUCED_HEIGHT, REDUCED_WIDTH, 3), np.uint8)
cv.imshow('Overlay', overlay)
cv.moveWindow('Overlay', 0, 0)
cv.setWindowProperty('Overlay', cv.WND_PROP_TOPMOST, 1)
setClickthrough('Overlay')

display_image = False

while True:
    # ret, img = vid.read()
    # img = cv.imread('test.jpg')
    img = screen_grab('chrome')
    img = cv.medianBlur(img, 5)
    img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img = cv.resize(img, (REDUCED_WIDTH, REDUCED_HEIGHT), interpolation=cv.INTER_LINEAR)

    overlay = np.zeros((REDUCED_HEIGHT, REDUCED_WIDTH, 3), np.uint8)

    knives = cascade.detectMultiScale(img, scaleFactor=1.01, minNeighbors=100, minSize=(24, 24), maxSize=(150, 150))

    for (x, y, w, h) in knives:
        # print("Knife detected")
        if display_image:
            cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        else:
            cv.rectangle(overlay,(x,y),(x+w,y+h),(255,0,0),2)
    
    if display_image:
        overlay = cv.resize(img, (WIDTH, HEIGHT), interpolation=cv.INTER_NEAREST)
    else:
        overlay = cv.resize(overlay, (WIDTH, HEIGHT), interpolation=cv.INTER_NEAREST)
    cv.imshow('Overlay', overlay)
    cv.waitKey(1)