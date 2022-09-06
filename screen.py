from PIL import Image, ImageGrab
import win32gui, win32ui
from ctypes import windll
import numpy as np
import time

# def screen_grab(win_name):
#     toplist, winlist = [], []
#     def enum_cb(hwnd, results):
#         winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
#     win32gui.EnumWindows(enum_cb, toplist)

#     window = [(hwnd, title) for hwnd, title in winlist if win_name in title.lower()]
#     # just grab the hwnd for first window matching 'win_name'
#     window = window[0]
#     hwnd = window[0]

#     # win32gui.SetForegroundWindow(hwnd)  # Set focus on found window
#     bbox = win32gui.GetWindowRect(hwnd)
#     img = ImageGrab.grab(bbox)
#     img = np.array(img.convert('RGB'))  # Convert img to np array
#     img = img[:, :, ::-1].copy()  # Convert RGB to BGR
#     return img

def screen_grab(win_name):
    toplist, winlist = [], []
    def enum_cb(hwnd, results):
        winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
    win32gui.EnumWindows(enum_cb, toplist)

    window = [(hwnd, title) for hwnd, title in winlist if win_name in title.lower()]
    # just grab the hwnd for first window matching 'win_name'
    window = window[0]
    hwnd = window[0]

    # Change the line below depending on whether you want the whole window
    # or just the client area. 
    #left, top, right, bot = win32gui.GetClientRect(hwnd)
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    w = right - left
    h = bot - top

    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC  = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    saveBitMap = win32ui.CreateBitmap()
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)

    saveDC.SelectObject(saveBitMap)

    # Change the line below depending on whether you want the whole window
    # or just the client area. 
    #result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 3)

    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)

    img = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1)

    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    img = np.array(img.convert('RGB'))  # Convert img to np array
    img = img[:, :, ::-1].copy()  # Convert RGB to BGR
    return img
