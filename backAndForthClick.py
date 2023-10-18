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

# Initialize global variables to hold destination and next destination
dest_x, dest_y = 0, 0
ndest_x, ndest_y = 0, 0

running = True



def dest_for_mouse():
    global dest_x, dest_y
    root = tk.Tk()
    root.geometry("1280x540")
    root.title("Destination for Mouse")
    
    def close():
        root.destroy()

    text = tk.Label(root, text="To start the script, press 'Ready,' and then a countdown for 3 seconds will begin for the first mouse location. Hover the mouse pointer over the destination!")
    text.place(x=70, y=90)
    exit_button = tk.Button(root, text="Ready", command=close)
    exit_button.pack(padx=60, pady=20)

    root.mainloop()
    time.sleep(3)
    dest_x, dest_y = pyautogui.position()
    print("Phase 1 done!!!")

def next_dest_for_mouse():
    global ndest_x, ndest_y
    root = tk.Tk()
    root.geometry("1280x540")
    root.title("Next Destination for Mouse")

    def close():
        root.destroy()

    text = tk.Label(root, text="To determine the 2nd mouse pointer's destination, press 'Ready,' and a countdown of 3 seconds will begin.")
    text.place(x=70, y=90)
    exit_button = tk.Button(root, text="Ready", command=close)
    exit_button.pack(padx=60, pady=20)

    root.mainloop()
    time.sleep(3)
    ndest_x, ndest_y = pyautogui.position()
    print("Phase 1 done!!!")

def check_esc_key():
    global running
    while running:
        if pyautogui.hotkey("esc"):
            print("Exiting the code")
            running = False

def submit():
    global running
    password = passw_var.get()
    root.destroy()
    
    if password.lower() == 'start':
        dest_for_mouse()
        next_dest_for_mouse()
        print("Destination:", dest_x, dest_y)
        print("Next Destination:", ndest_x, ndest_y)
        print("Test passed")


        while running:
            c1 = random.randint(dest_x, ndest_x)
            c2 = random.randint(dest_y, ndest_y)
            time.sleep(1)
            pyautogui.moveTo(c1, c2)
            pyautogui.click()
            time.sleep(1)
            c1 = random.randint(dest_x, ndest_x)
            c2 = random.randint(dest_y, ndest_y)
            pyautogui.moveTo(c1, c2)
            pyautogui.click()
            if win32api.GetAsyncKeyState(win32con.VK_ESCAPE) != 0:
                print("Stopping the script.")
                break


root = tk.Tk()
root.geometry("600x400")
root.title("Mouse Automation")

passw_var = tk.StringVar()

passw_label = tk.Label(root, text='Press "start" to continue:', font=('calibre', 10, 'bold'))
passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'))
sub_btn = tk.Button(root, text='Submit', command=submit)

passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

root.mainloop()
