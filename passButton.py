import pyautogui

from datetime import datetime
import datetime as dt
import os

found = False

pyautogui.PAUSE = 0.01
click = 0
# For windows
if os.name == "nt":
    while click < 5:
        if (
            pyautogui.locateOnScreen("click.png", grayscale=True, confidence=0.9)
            != None
            and found == False
        ):
            pyautogui.moveTo("click.png")
            found = True

        if found == True:
            pyautogui.click()
            print("Clicking")
            click += 1

        print(datetime.now())
# For macOS
else:
    while click < 5:
        if (
            pyautogui.locateOnScreen("macClick.png", grayscale=True, confidence=0.9)
            != None
            and found == False
        ):
            target = pyautogui.locateOnScreen(
                "macClick.png", grayscale=True, confidence=0.9
            )
            targetLoc = pyautogui.center(target)
            target_x, target_y = targetLoc
            pyautogui.moveTo(target_x / 2, target_y / 2)
            found = True

        if found == True:
            pyautogui.click()
            print("Clicking")
            click += 1

        print(datetime.now())
