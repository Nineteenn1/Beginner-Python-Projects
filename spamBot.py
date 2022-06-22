import pyautogui as spam
import time
timeout = time.time() + 90 #Change the 30 here to an other number if you want it to last longer or shorter
while True:
    test = 0
    spam.typewrite("@everyone")
    spam.press('enter')
    if test == 90 or time.time() > timeout: # and here
        break
    test = test -1
    time.sleep(1)
 
