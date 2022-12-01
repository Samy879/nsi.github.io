import pyautogui
import keyboard
import time

print("Pour arrêter ce programme, appuyez sur la flèche du bas ↓")
time.sleep(1)

while True:
    a = pyautogui.position()
    time.sleep(0.08)
    b = pyautogui.position()

    x, y = b

    if a != b:
        print("("+str(x)+" ; "+str(y)+")")

    if keyboard.is_pressed("down"):
        break
