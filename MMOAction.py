import keyboard
import pyautogui
from screeninfo import get_monitors

hotkey_hold_right_mouse = "shift+alt"
hotkey_kill_script = "shift+alt+ctrl"

height = 0
width = 0

print("MMO Action is now running!\n")
print("HOW TO USE:\n")
print("Press SHIFT + ALT to lock your right mouse button into action camera.\n")
print("Pressing the right mouse button while it locked, will release it. You will have to press SHIFT + ALT again to lock it back into action camera.\n")
print("Press SHIFT + ALT + CTRL to kill the script.\n")

for m in get_monitors():
    if m.is_primary:
        height = m.height / 2
        width = m.width / 2


def lock_right_mouse_button():
    pyautogui.moveTo(width, height)
    pyautogui.mouseDown(button="right")


def release_right_mouse_button():
    pyautogui.mouseUp(button="right")


keyboard.add_hotkey(hotkey_hold_right_mouse, lock_right_mouse_button)
keyboard.add_hotkey(hotkey_kill_script, release_right_mouse_button)

try:
    keyboard.wait(hotkey_kill_script)
except Exception as e:
    print(e)

keyboard.remove_hotkey(hotkey_hold_right_mouse)