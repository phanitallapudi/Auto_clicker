import win32api
import win32con
import time

def press_key(key_code, duration=1):
    win32api.keybd_event(key_code, 0, 0, 0)
    time.sleep(duration)
    win32api.keybd_event(key_code, 0, win32con.KEYEVENTF_KEYUP, 0)

def main():
    print("Press Esc to stop the script.")
    
    space_key = 0x20  # Space key code
    backspace_key = 0x08  # Backspace key cod
    # Loop until the Esc key is pressed
    while True:
        if win32api.GetAsyncKeyState(win32con.VK_ESCAPE):
            print("Stopping the script.")
            break

        press_key(space_key)  # Press Space
        press_key(backspace_key)  # Press Backspace

if __name__ == "__main__":
    main()
