import keyboard
import pyautogui
while True:
    if keyboard.read_key() == "/":
        mouse = pyautogui.position()
        print(mouse)
        break
