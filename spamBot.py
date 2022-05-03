import pyautogui as spam
import time
timeout = time.time() + 30 #Change the 30 here to an other number if you want it to last longer or shorter
while True:
    time.sleep(1)
    test = 0
    spam.typewrite("Spam Eggs Bacon")
    spam.press('enter')
    if test == 30 or time.time() > timeout: # and here
        break
    test = test -1
    
 
