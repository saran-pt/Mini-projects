import pyautogui
import time

message = ['vimbin', 'bipas', 'ludo']
def spam_bot():
    time.sleep(10)
    a = 10
    while a > 0:
        for line in message:
            pyautogui.typewrite(line)
            pyautogui.press('enter')
        a -= 1

spam_bot()