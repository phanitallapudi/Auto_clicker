import subprocess
import sys
import time
import random

# Check if a module is installed
def is_module_installed(module_name):
    try:
        __import__(module_name)
        return True
    except ImportError:
        return False

# Install a package using pip
def install_package(package_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])

# Ensure pywin32 is installed
if not is_module_installed("pywin32"):
    print("pywin32 is not installed. Installing it now...")
    install_package("pywin32")
    print("pywin32 has been successfully installed.")

import win32api
import win32con

def press_key(key_code, duration=1):
    win32api.keybd_event(key_code, 0, 0, 0)
    time.sleep(duration)
    win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

def main():
    time.sleep(2)
    print("Press Esc to stop the script.")
    
    space_key = 0x20  # Space key code
    backspace_key = 0x08  # Backspace key code

    keys = [ord('A'), ord('B'), ord('C'), ord('D'), ord('E'), ord('F'), ord('G'), ord('H'), ord('I'), ord('J'), ord('K'), ord('L'), ord('M'), ord('N'), ord('O'), ord('P'), ord('Q'), ord('R'), ord('S'), ord('T'), ord('U'), ord('V'), ord('W'), ord('X'), ord('Y'), ord('Z')]

    while True:
        if win32api.GetAsyncKeyState(win32con.VK_ESCAPE) != 0:
            print("Stopping the script.")
            break

        count = random.randint(1, 6)
        chosen = []
        for i in range(count):
            choice = random.choice(keys)
            chosen.append(choice)
        
        if win32api.GetAsyncKeyState(win32con.VK_ESCAPE) != 0:
            print("Stopping the script.")
            break

        for i in chosen:
            press_key(i)  
            time.sleep(1) 
        for i in range(len(chosen)):     
            press_key(backspace_key)  
        
        if win32api.GetAsyncKeyState(win32con.VK_ESCAPE) != 0:
            print("Stopping the script.")
            break

if __name__ == "__main__":
    main()

    
