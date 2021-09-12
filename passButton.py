import pyautogui
import keyboard
from datetime import datetime


screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
currentMouseX, currentMouseY = pyautogui.position()
found = False
pyautogui.PAUSE = 0.01
while keyboard.is_pressed("q") == False:
    if (
        pyautogui.locateOnScreen("click.png", grayscale=True, confidence=0.9) != None
        and found == False
    ):
        pyautogui.moveTo("click.png")
        found = True

    if found == True:
        pyautogui.click()

    print(datetime.now())
