import pyautogui
from pynput.keyboard import Key, Controller
import collections
import time
import tkinter

Point = collections.namedtuple('Point', 'x y')

offset = 20
corner_screen_1 = Point(0, 0)
corner_screen_2 = Point(-1920, 163)
delay_loop = 0.05
activated = False


def activate_windows_tab():
    Controller().press(Key.cmd)
    Controller().press(Key.tab)
    Controller().release(Key.cmd)
    Controller().release(Key.tab)


while True:
    time.sleep(delay_loop)
    if activated:
        time.sleep(0.5)
        activated = False
        continue
    mouse_position = pyautogui.position()
    if mouse_position.x <= corner_screen_1.x + 20 and mouse_position.y <= corner_screen_1.y + 20:
        activate_windows_tab()
        activated = True
    elif mouse_position.x <= corner_screen_2.x + 20 and mouse_position.y <= corner_screen_2.y + 20:
        activate_windows_tab()
        activated = True

