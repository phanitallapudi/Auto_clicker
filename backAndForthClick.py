import subprocess
import sys
import time

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
    print("Press Esc to stop the script.")
    
    space_key = 0x20  # Space key code
    backspace_key = 0x08  # Backspace key code

    while True:
        if win32api.GetAsyncKeyState(win32con.VK_ESCAPE) != 0:
            print("Stopping the script.")
            break

        press_key(space_key)  # Press Space
        time.sleep(0.5)  # Wait for 0.5 seconds
        press_key(backspace_key)  # Press Backspace

if __name__ == "__main__":
    main()
