from PIL import Image
import numpy as np
from multiprocessing import Process, freeze_support
import pyscreenshot as ImageGrab
import win32api, win32con, win32com.client
import webbrowser
import time


def click(x, y, times):
    # print("Clicked X: {0} Y: {1}".format(x, y))
    win32api.SetCursorPos((x, y))
    for i in range(0, times):
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        time.sleep(0.005)

def grab():
    im = ImageGrab.grab()
    return im

def main():
    print("""---Steam summer games 2018 bot---
    press "ctrl + alt + delete" to stop""")

    splashimg = np.array([[19, 20, 34], [20, 20, 34]])
    gameArea = []
    shell = win32com.client.Dispatch("WScript.Shell")
    checkForGameArea = True

    webbrowser.open("steam://openurl/https://steamcommunity.com/saliengame/play/")

    while True:

        while (checkForGameArea):
            time.sleep(1.5)

            print("Looking for game area")

            im = grab()
            im = np.array(im)

            print("Looking at screen: {1}x{0}".format(str(len(im)), str(len(im[0]))))

            if (checkForGameArea):
                if (checkForGameArea):
                    for x in range(0, len(im)):
                        for y in range(0, len(im[x])):
                            # print("X: {0} Y: {1} Value: {2}".format(str(x), str(y), str(im[x][y])))
                            if ((np.array_equal(splashimg[0], im[x][y])) and (np.array_equal(splashimg[1], im[x + 1][y]))):
                                print("Found top left corner at X: {0} Y: {1}".format(str(x), str(y)))
                                gameArea.append(y)
                                gameArea.append(x)
                                brX = y + 1280
                                brY = x + 720
                                print("Asuming bottom right corner is at X: {0} Y: {1}".format(str(brY), str(brX)))
                                gameArea.append(brX)
                                gameArea.append(brY)
                                checkForGameArea = False

            if (not len(gameArea) > 0):
                print("""Game area not found
                Make sure it's on your main display
                Make sure it's scolled all the way up
                Make sure you have the summer saliens game open on it's main menu
                https://steamcommunity.com/saliengame/play/""")

        if (len(gameArea) > 0):
            # im = ImageGrab.grab(bbox=(gameArea))
            # im.show()

            click(gameArea[0] + 640, gameArea[1] + 470, 1)

            time.sleep(6
                       )

            for i in range(0, 12):
                for j in range(0, 8):
                    click(gameArea[0] + (440 + (67 * i)), gameArea[1] + (132 + (67 * j)), 1)
                    time.sleep(0.01)
                    click(gameArea[0] + 1, gameArea[1] + 1, 1)
                    time.sleep(0.025)
            time.sleep(5)
            timeout = time.time() + 123
            while True:
                for i in range(300, 650, 25):
                    click(gameArea[0] + 1100, gameArea[1] + i, 5)
                    for key in range(1, 6):
                        shell.SendKeys(str(key))
                    #time.sleep(0.01)
                if time.time() > timeout:
                    break
            time.sleep(1)
            click(gameArea[0] + 648, gameArea[1] + 460 , 1)
            time.sleep(2.5)


if __name__ == '__main__':
    freeze_support()
    p = Process(target=grab)
    p.start()
    main()
