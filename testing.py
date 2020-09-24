import pyautogui
import math
import time
import keyboard

dicepos = (200, 920)
dicespacing = 167
chestpos = (392, 624)
chestspacing = 121
failuredice = [1, 2, 4, 1]
# failuredice = [1]
# failuredice = [2, 1]
optimal = 5.485
screen = 1920
loop = True


def checkpixelcolor(x, y, r, g, b):
    pixel = pyautogui.pixel(screen + x, y)
    if pixel[0] == r and pixel[1] == g and pixel[2] == b:
        return True
    else:
        return False


def detectkey():
    if keyboard.is_pressed("`"):
        print("Exiting...")
        exit(0)


def isplayersturn():
    pixel1 = pyautogui.pixel(screen + 157, 130)
    pixel2 = pyautogui.pixel(screen + 291, 118)
    if pixel1[0] == pixel2[0] and pixel1[1] == pixel2[1] and pixel1[2] == pixel2[2] and pixel1[0] == 218 and pixel1[
        1] == 165 and pixel1[2] == 32:
        return True
    else:
        return False


def islootcrates():
    if checkpixelcolor(640, 265, 0, 198, 255) and checkpixelcolor(640, 290, 59, 86, 125) and checkpixelcolor(640, 320, 255, 255, 255):
        return True
    else:
        return False


def isplayerturnlong(timetocheck):
    for i in range(timetocheck * 10):
        if isplayersturn():
            return True
        else:
            time.sleep(0.1)
    return False


def waittilplayerturn():
    counter = 0
    while not isplayersturn():
        time.sleep(5)
        detectkey()
        counter += 1
        if islootcrates() and loop:
            restart()
            break
        if counter >= 12:
            exit()


def collect():
    pyautogui.moveTo(screen + 150, 600)
    pyautogui.dragTo(screen + 1700, 600, 1)


def roll(times):
    for i in range(times):
        for j in range(4):
            pyautogui.click(screen + 200 + dicespacing * j, 920)
        time.sleep(1)  # only needs 0.6 secs for dice to be clickable again
        pixel = pyautogui.pixel(screen + 1461, 858)
        if pixel[0] != 255 or pixel[1] != 255 or pixel[2] != 255:
            # print("ROLLED A 1!")
            time.sleep(1.5)
            return
    pyautogui.click(screen + 1461, 858)
    time.sleep(4)
    collect()


def rollround():
    detectkey()
    for i in range(len(failuredice)):
        detectkey()
        if isplayerturnlong(1):
            print("taking go for monster " + str(i))
            roll(math.floor((optimal / failuredice[i]) + 0.5))
        else:
            break
    collect()


def docrates():
    for i in range(7):
        pyautogui.click(screen + 900, 300)
        time.sleep(1)
    for i in range(10):
        pyautogui.click(screen + chestpos[0] + i*chestspacing, chestpos[1])
    collect()
    collect()
    collect()
    collect()
    pyautogui.click(screen + 900, 500)
    time.sleep(2);


def doendseq():
    pyautogui.click(screen + 1600, 950)
    time.sleep(1)
    pyautogui.click(screen + 1600, 950)
    time.sleep(5)
    pyautogui.click(screen + 1600, 950)
    time.sleep(1)
    pyautogui.click(screen + 1600, 950)
    time.sleep(1)
    pyautogui.click(screen + 1600, 950)
    time.sleep(1)
    pyautogui.click(screen + 1600, 950)
    time.sleep(1)
    pyautogui.click(screen + 1600, 950)
    time.sleep(1)


def dostartseq():
    pyautogui.click(screen + 1300, 500)
    time.sleep(1)
    pyautogui.click(screen + 1600, 950)


def restart():
    docrates()
    doendseq()
    dostartseq()

dostartseq()
while True:
    detectkey()
    waittilplayerturn()
    rollround()
