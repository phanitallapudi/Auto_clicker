
import time
from pynput.mouse import Listener


def is_clicked(x, y, button, pressed):
    if pressed:
        return button

with Listener(on_click=is_clicked) as listener:
    listener.join()