import sys
import subprocess

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

modules = ["pywin32", "pyautogui"]

for module in modules:
    try:
        __import__(module)
    except ImportError:
        install(module)

import tkinter as tk
import pyautogui
import time
import random
import win32api
import win32con

running = True

def dest_for_mouse():
    def close():
        root.destroy()
    global dest_x, dest_y
    root = tk.Tk()
    root.geometry("1280x370")
    root.title("Destination for Mouse")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(padx=20, pady=20)

    text = tk.Label(frame, text="Welcome to the Mouse Destination Script", font=('calibri', 14, 'bold'))
    text.pack(pady=(0, 20))

    instructions = tk.Label(frame, text="To start the script, press 'Ready,' and then a countdown for 3 seconds will begin for the first mouse location.\nHover the mouse pointer over the destination!", font=('calibri', 12))
    instructions.pack()

    exit_button = tk.Button(frame, text="Ready", command=close, font=('calibri', 12, 'bold'))
    exit_button.pack(pady=20)

    root.mainloop()

    time.sleep(3)
    print("Phase 1 done!!!")
    return pyautogui.position()

def next_dest_for_mouse():
    def close():
        root.destroy()
    global ndest_x, ndest_y
    root = tk.Tk()
    root.geometry("640x270")
    root.title("Next Destination for Mouse")

    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(padx=20, pady=20)

    instructions = tk.Label(frame, text="To determine the 2nd mouse pointer's destination,\npress 'Ready,' and a countdown of 3 seconds will begin.", font=('calibri', 12))
    instructions.pack()
    exit_button = tk.Button(frame, text="Ready", command=close, font=('calibri', 12, 'bold'))
    exit_button.pack(pady=20)

    root.mainloop()
    time.sleep(3)
    print("Phase 2 done!!!")
    return pyautogui.position()

def press_key(key_code, duration=1):
    win32api.keybd_event(key_code, 0, 0, 0)
    time.sleep(duration)
    win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

def submit():
    global running
    password = passw_var.get()
    root.destroy()
    
    dest_x, dest_y = 0, 0
    ndest_x, ndest_y = 0, 0

    if password.lower() == 'custom':
        dest_x, dest_y = dest_for_mouse()
        ndest_x, ndest_y = next_dest_for_mouse()
    elif password.lower() == 'default':
        dest_x, dest_y = 950, 140
        ndest_x, ndest_y = 1800, 450
    print("Destination:", dest_x, dest_y)
    print("Next Destination:", ndest_x, ndest_y)
    print("Waiting 5 seconds for you to setup")
    time.sleep(5)

    backspace_key = 0x08
    keys = [ord('A'), ord('B'), ord('C'), ord('D'), ord('E'), ord('F'), ord('G'), ord('H'), ord('I'), ord('J'), ord('K'), ord('L'), ord('M'), ord('N'), ord('O'), ord('P'), ord('Q'), ord('R'), ord('S'), ord('T'), ord('U'), ord('V'), ord('W'), ord('X'), ord('Y'), ord('Z')]

    while running:
        
        c1 = random.randint(dest_x, ndest_x)
        c2 = random.randint(dest_y, ndest_y)
        time.sleep(1)
        pyautogui.moveTo(c1, c2, duration=random.uniform(0.2, 0.5))
        pyautogui.click()
        time.sleep(1)
        count = random.randint(1, 6)
        chosen = []
        for i in range(count):
            choice = random.choice(keys)
            chosen.append(choice)
        for i in chosen:
            press_key(i)  
            time.sleep(1)
        for i in range(len(chosen)):    
            press_key(backspace_key)  
        c1 = random.randint(dest_x, ndest_x)
        c2 = random.randint(dest_y, ndest_y)
        pyautogui.moveTo(c1, c2, duration=random.uniform(0.2, 0.5))
        pyautogui.click()

        time.sleep(1)
        scroll_amount = random.randint(-300, 300)  # Adjust the range to control scrolling
        pyautogui.scroll(scroll_amount)
        if win32api.GetAsyncKeyState(win32con.VK_ESCAPE) != 0:
            print("Stopping the script.")
            break



root = tk.Tk()
root.geometry("600x400")
root.title("Mouse Automation")

passw_var = tk.StringVar()

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(padx=20, pady=20)

passw_var = tk.StringVar(value="custom")  # Set the default value to "custom"

passw_label = tk.Label(frame, text='Please select an option:', font=('calibri', 12, 'bold'))
passw_label.pack(pady=(0, 10))

custom_radio = tk.Radiobutton(frame, text="Custom Settings (Press 'C' or 'custom')", variable=passw_var, value="custom", font=('calibri', 10))
custom_radio.pack()

default_radio = tk.Radiobutton(frame, text="Default Settings (Press 'D' or 'default')", variable=passw_var, value="default", font=('calibri', 10))
default_radio.pack()

sub_btn = tk.Button(frame, text='Submit', command=submit, font=('calibri', 10, 'bold'))
sub_btn.pack()

root.mainloop()
