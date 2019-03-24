import pyautogui
from pynput.keyboard import Key, Controller
import collections
import time

Point = collections.namedtuple('Point', 'x y')

offset = 20
corner_screen_1 = Point(0, 0)
corner_screen_2 = Point(-1920, 163)
corner_screens = []
delay_loop = 0.05
activated = False


def activate_windows_tab():
    Controller().press(Key.cmd)
    Controller().press(Key.tab)
    Controller().release(Key.cmd)
    Controller().release(Key.tab)


f = open("position-corner.txt", "r")
lines = f.readlines()
for line in lines:
    positions_splited = line.split(",")
    next_corner = Point(int(positions_splited[0]), int(positions_splited[1]))
    corner_screens.append(next_corner)


while True:
    time.sleep(delay_loop)
    if activated:
        time.sleep(0.5)
        activated = False
        continue
    mouse_position = pyautogui.position()
    for corner in corner_screens:
        if mouse_position.x <= corner.x + offset and mouse_position.y <= corner.y + offset:
            activate_windows_tab()
            activated = True

