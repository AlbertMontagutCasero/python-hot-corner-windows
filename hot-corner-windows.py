import pyautogui
from pynput.keyboard import Key, Controller
import collections
import time
import wmi


def get_processes_by_process_name(process_name):
    global winmi
    if winmi is None:
        print("winmi none")
        winmi = wmi.WMI()

    processes = []
    for process in winmi.Win32_Process():
        if process.name == process_name:
            processes.append(process)

    if len(processes) <= 0:
        return None

    return processes


def terminate_all_processes_except_one(processes):
    for i in range(len(processes) - 1):
        processes[i].Terminate()


def activate_windows_tab():
    Controller().press(Key.cmd)
    Controller().press(Key.tab)
    Controller().release(Key.cmd)
    Controller().release(Key.tab)


winmi = None

process_name = 'hot-corner-windows.exe'
processes = get_processes_by_process_name(process_name)
if processes is not None:
    terminate_all_processes_except_one(get_processes_by_process_name(process_name))

corner_screens = []
delay_loop = 0.1
Coordinates = collections.namedtuple('Point', 'left_x top_y right_x bottom_y')

file = open("position-corner.txt", "r")
lines = file.readlines()
for line in lines:
    line = line.strip()
    line = line.split(';')
    positions_split = line[0].split(',')
    positions_offset_split = line[1].split(",")
    next_corner = Coordinates(
        int(positions_split[0]), int(positions_split[1]),
        int(positions_offset_split[0]), int(positions_offset_split[1]))
    corner_screens.append(next_corner)

last_position_was_in_area = False
iteration_in_area = False

while True:
    time.sleep(delay_loop)
    mouse_position = pyautogui.position()
    for corner in corner_screens:
        if (corner.left_x <= mouse_position.x <= corner.right_x) and (
                corner.top_y <= mouse_position.y <= corner.bottom_y):
            iteration_in_area = True
            if not last_position_was_in_area:
                activate_windows_tab()

    last_position_was_in_area = iteration_in_area
    iteration_in_area = False
