#pip install pyautogui
#pip install pywin32
#pip install tkinter


from tkinter import *                                                               #modules required to run the script 
import subprocess
import sys
import time


try:
    loop_for_packages = True
    while loop_for_packages:                                                                                #this script is almost automated, every module required will be download if not present in the host system
        def install(package):
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])    #This function uses subprocess package to install the modules if not found
        x = 'pyautogui'
        y = 'pynput'                                                                    #except these 3 package, every other used package in this script are preloaded with python
        z = 'pywin32'

        if x in sys.modules and y in sys.modules and z in sys.modules:                  #if 'pyautogui', 'pynput' and 'pywin32' are pre-installed, then this if-else statement will be ignored
            loop_for_packages = False                                                                
        else:                                                                           #if the above 3 mentioned modules are not present, then it will install those modules using the install function mentioned above. Note: Requires internet conncetion for the first time.
            if x not in sys.modules:
                install(x)
            elif y not in sys.modules:
                install(y)
            elif z not in sys.modules:
                install(z)
            else:
                pass
except:
    print("no internet.")

                                                                                    #exception handling done for no internet connection.
import win32api
import pyautogui

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
    
    if password == 'no' or password == 'NO' or password == 'No':                    #here after selecting 'no' in the first Tkinter UI, you will be asked to hover the mouse pointer to get the destionation of the mouse to where you need to click.
        dest_x, dest_y = dest_for_mouse()                                           #the function named 'dest_for_mouse()' will be the one for the first mouse pointer destination
        ndest_x, ndest_y = next_dest_for_mouse()                                    #the function named 'next_dest_for_mouse()' will be used for the second destionation of the mouse pointer to end up.
        print(dest_x, dest_y)
        print(ndest_x, ndest_y)

        print("Test passed")
        m = True
        while m:
            left_click = win32api.GetKeyState(0x01)
            esc_click = win32api.GetKeyState(0x1B)

            if left_click < 0:
                print("Left click")
            time.sleep(0.1)
            if esc_click < 0:
                print("Exiting the code")
                m = False
    else:
        pass
#the first user interface will start from here.    
import tkinter as tk

root = tk.Tk()                                                                        
root.geometry("600x400") 
name_var = tk.StringVar()
passw_var = tk.StringVar()                                                          #Using tkinter we will be asked whether to use preloaded settings i.e., examly or custom settings

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









