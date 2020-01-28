import pyautogui
import time

def det():
    time.sleep(1)
    start = pyautogui.locateCenterOnScreen('tu.png')
    print(start)
    det.start = start 
    if start == None:
        scroll()
    else:
        delete()


def delete():
    start = det.start
    pyautogui.moveTo(start)
    pyautogui.doubleClick()
    pyautogui.click(start)
    pyautogui.press('del')
    det()

def scroll():
    pyautogui.scroll(-1000)
    det()

det()
