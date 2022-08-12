
from pynput.mouse import Listener
from tkinter import *
import subprocess
import sys
import pyautogui
import time

try:
    def install(package):
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    x = 'pyautogui'
    y = 'pynput'

    if x in sys.modules and y in sys.modules:
        pass
    else:
        install(x)
        install(y)
except:
    print("no internet.")


    
import tkinter as tk

root=tk.Tk()
root.geometry("600x400") 
name_var=tk.StringVar()
passw_var=tk.StringVar()

def Close():
    root.destroy()
def dest_for_mouse():
    def Close():
        root.destroy()
    root = Tk()
    root.geometry("1280x540")

    text = Label(text="To start the script press ready and then the countdown for 3 seconds start for the destination of the first click, however the mouse pointer over there!!!")
    text.place(x=70,y=90)
    exit_button = Button(root, text="Ready", command=Close)
    exit_button.pack(padx=60,pady=20)
        
    root.mainloop()
    time.sleep(5)
    a,b = pyautogui.position()
        #####################################

    print("Phase 1 done!!!")
    return a, b

def next_dest_for_mouse():
    root = Tk()
    root.geometry("1280x540")
    def Close():
        root.destroy()

    text = Label(text="Now we need to take input for the mouse pointer to comeback, press ready to start and counter will be for 5 seconds")
    text.place(x=70,y=90)
    exit_button = Button(root, text="Ready", command=Close)
    exit_button.pack(padx=60,pady=20)
        
    root.mainloop()
    time.sleep(5)

    end_x,end_y = pyautogui.position()
    return (end_x, end_y)

def submit():
    
    name=name_var.get()
    password=passw_var.get()
    #####################################
        
    #print(password)
    #####################################
        
    name_var.set("")
    passw_var.set("")
    root.destroy()
    
    if password == 'no' or password == 'NO' or password == 'No':
        dest_x, dest_y = dest_for_mouse()
        print(dest_x, dest_y)
        ndest_x, ndest_y = next_dest_for_mouse()
        print(ndest_x, ndest_y)

        status = True
        while status:
            def is_clicked(x, y, button, pressed):
                
                if pressed:

                    time.sleep(1)
                    pyautogui.click(dest_x,dest_y)
                    time.sleep(1)
                    pyautogui.click(ndest_x,ndest_y)

            with Listener(on_click=is_clicked) as listener:
                listener.join()
    else:
        def is_clicked(x, y, button, pressed):
            if pressed:
                    time.sleep(1)
                    pyautogui.click(1450,1010)
                    time.sleep(1)
                    pyautogui.click(780,330)

        with Listener(on_click=is_clicked) as listener:
            listener.join()

name_label = tk.Label(root, text = 'press yes for examly settings and no for custom', font=('calibre',10, 'bold'))
    
name_entry = tk.Entry(root,textvariable = name_var, font=('calibre',10,'normal'))
    
passw_label = tk.Label(root, text = 'Yes/No', font = ('calibre',10,'bold'))
passw_entry=tk.Entry(root, textvariable = passw_var, font = ('calibre',10,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = submit)

name_label.grid(row=1,column=0)
#name_entry.grid(row=0,column=1)
passw_label.grid(row=2,column=0)
passw_entry.grid(row=2,column=1)
sub_btn.grid(row=3,column=1)
root.mainloop()









