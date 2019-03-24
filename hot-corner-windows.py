import pyautogui
from pynput.keyboard import Key, Controller
import collections
import time

Point = collections.namedtuple('Point', 'x y offset_x offset_y')

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
    line = line.strip()
    line = line.split(';')
    positions_split = line[0].split(',')
    positions_offset_split = line[1].split(",")
    next_corner = Point(
        int(positions_split[0]), int(positions_split[1]),
        int(positions_offset_split[0]), int(positions_offset_split[1]))
    corner_screens.append(next_corner)


while True:
    time.sleep(delay_loop)
    if activated:
        time.sleep(0.5)
        activated = False
        continue
    mouse_position = pyautogui.position()
    for corner in corner_screens:
        if mouse_position.x <= corner.x + corner.offset_x and mouse_position.y <= corner.y + corner.offset_y:
            activate_windows_tab()
            activated = True

