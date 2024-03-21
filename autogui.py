import pyautogui
import time

#Move the mouse to coordinate (100, 100) and click
pyautogui.moveTo(100, 100, duration=1)
pyautogui.click()

#Type a message
pyautogui.typewrite("Hello World!")

#Take screenshot and save it
scrrenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')
