import keyboard
import pyautogui
import os
import re
from screeninfo import get_monitors

height = 0
width = 0


def create_hotkeys_file():
    file_name = "hotkeys.txt"

    if not os.path.exists(file_name):
        with open(file_name, "w"):
            pass


def read_hotkeys_file():
    file_name = "hotkeys.txt"

    with open(file_name, "r") as file:
        content = file.read()

        if not content == "":
            elements = content.split(',')
            cleaned_elements = [element.strip() for element in elements]

            if len(cleaned_elements) == 1:
                return [cleaned_elements[0]]
            else:
                return cleaned_elements

    return "", ""


for m in get_monitors():
    if m.is_primary:
        height = m.height / 2
        width = m.width / 2


def lock_right_mouse_button():
    pyautogui.moveTo(width, height)
    pyautogui.mouseDown(button="right")


def release_right_mouse_button():
    pyautogui.mouseUp(button="right")


try:
    create_hotkeys_file()
    hotkey_hold_right_mouse, hotkey_kill_script = read_hotkeys_file()

    if hotkey_hold_right_mouse == "":
        hotkey_hold_right_mouse = "shift+alt"

    if hotkey_kill_script == "":
        hotkey_kill_script = "shift+alt+ctrl"

    keyboard.add_hotkey(hotkey_hold_right_mouse, lock_right_mouse_button)
    keyboard.add_hotkey(hotkey_kill_script, release_right_mouse_button)

    print(f"""MMOAction is now running!
    
Press "{hotkey_hold_right_mouse.upper()}" to lock your "RIGHT MOUSE BUTTON" into "Action Camera Mode".
    
If you press your "RIGHT MOUSE BUTTON" while in "Action Camera Mode", you will have to press "{hotkey_hold_right_mouse.upper()}" again to go back to "Action Camera Mode".
    
Press "{hotkey_kill_script.upper()}" to kill the script.

You can change the above hotkeys by closing MMOAction, and adding your own set of hotkeys in the "hotkeys.txt" file inside the root folder.

Read the instructions below:

You do not add "[]" into the file, they are here just to make the example better to understand.

[a,esc] <- Changes the default "Action Camera Mode" hotkey to "a", and changes the default hotkey to kill the script to "esc".

[,esc] <- Keep the default "Action Camera Mode" hotkey, and changes the default hotkey to kill script to "esc".

[a,] <- Changes the default "Action Camera Mode" hotkey to "a", and keep the default hotkey to kill the script.
""")

    keyboard.wait(hotkey_kill_script)
except Exception as e:
    print("An error was found:\n")

    if "unpack" in str(e):
        print(f"{e}\n")
        print("""You probably forgot to add "," to separate the hotkeys inside the hotkeys.txt file.\n""")
    else:
        print(f"{e}\n")

    input("Fix the above issues and restart MMOAction.\n")