import pyautogui
import time
import keyboard
import win32api
import win32con

def switch_tabs():
    try:
        while True:
            # Press Alt + Tab to switch between tabs
            pyautogui.hotkey('alt', 'tab')

            # Wait for 2 seconds
            time.sleep(2)

            # Check if the 'esc' key is pressed to stop the loop
            if win32api.GetAsyncKeyState(win32con.VK_ESCAPE) != 0:
                print("Stopping the script.")
                break
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Ensure the Alt key is not held down
        pyautogui.hotkey('alt', 'release')

if __name__ == "__main__":
    time.sleep(10)
    switch_tabs()
