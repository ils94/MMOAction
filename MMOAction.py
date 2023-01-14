import sys
import pyautogui
import subprocess
import keyboard
import time
from screeninfo import get_monitors

on = False

middle = None

height = 0
width = 0

tick = 0.1

for m in get_monitors():
    if m.is_primary:
        height = m.height / 2
        width = m.width / 2


def quick_exit():
    if keyboard.is_pressed("Shift"):
        if keyboard.is_pressed("Esc"):
            pyautogui.mouseUp(button="right")
            sys.exit()


def cursor():
    global middle

    option = input("Always move cursor to the middle of the screen? Y/N"
                   "\nInput: ")

    if option.upper() == "Y":
        middle = True
    elif option.upper() == "N":
        middle = False
    else:
        subprocess.run("cls", shell=True)
        cursor()

    subprocess.run("cls", shell=True)


cursor()

print("MMO Action is now running!\n")
print("HOW TO USE:\n")
print("Hold SHIFT + ALT to lock your right mouse button into action camera.\n")
print("Hold SHIFT + CTRL to release your right mouse button from action camera.\n")
print("Holding CAPSLOCK while the right mouse button is locked into action camera, will release it so you can interact "
      "with NPCs and objects in game. Releasing CAPSLOCK will lock your mouse back into action camera.\n")
print("Hold SHIFT + ESC to kill the program and release your mouse.")

while True:
    while on:
        if not keyboard.is_pressed("Shift"):
            if pyautogui.position().x != width and pyautogui.position().y != height and middle:
                pyautogui.moveTo(width, height)

            pyautogui.mouseDown(button="right")

        if keyboard.is_pressed("Shift"):
            pyautogui.mouseUp(button="right")

        if keyboard.is_pressed("Shift"):
            if keyboard.is_pressed("Ctrl"):
                pyautogui.mouseUp(button="right")
                on = False
        if not on:
            break

        quick_exit()

        time.sleep(tick)

    if keyboard.is_pressed("Shift") and not on:
        if keyboard.is_pressed("Alt"):
            on = True

    quick_exit()

    time.sleep(tick)
