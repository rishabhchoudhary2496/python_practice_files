import pyautogui;
import os

import pyscreeze

wh = pyautogui.size()
print(wh.width)
print(pyautogui.position())
pyautogui.moveTo(100, 100, duration=0.25)
pyautogui.moveTo(200, 100, duration=0.25)     
pyautogui.moveTo(200, 200, duration=0.25)
pyautogui.moveTo(10, 750, duration=0.25)
pyautogui.click()
pyautogui.write('spotify')
screenshot = pyautogui.screenshot()
screenshot.save(r"d:\\screenshot.png")
print(screenshot)