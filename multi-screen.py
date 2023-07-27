# multi-screen.py

import os
import subprocess
import tkinter as tk
from tkinter import messagebox
from pynput.keyboard import Controller, Key, KeyCode

def start_recording():
    try:
        keyboard = Controller()
        platform = os.sys.platform
        if platform == "win32":
            # For Windows, we will launch TowelScreenRecorder.exe
            subprocess.run(r"C:\Program Files\TowelScreenRecorder\TowelScreenRecorder.exe", shell=True)
            # Now we simulate pressing Shift + PrintScreen
            with keyboard.pressed(Key.shift):
                keyboard.press(KeyCode.from_vk(0x2C))  # VK_SNAPSHOT is the virtual key code for PrintScreen
                keyboard.release(KeyCode.from_vk(0x2C))
        elif platform == "darwin":
            # For MacOS, we will trigger the screenshot toolbar
            subprocess.run(["open", "-a", "Screenshot"])
        else:
            messagebox.showinfo("Not Supported", "Your OS is not supported by this program")

        # Minimize the tkinter window
        root.iconify()

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

root = tk.Tk()
root.title('Screen Recorder Launcher')
root.geometry('300x200')

button = tk.Button(root, text='Start Screen Recording', command=start_recording)
button.pack(fill='both', expand=True)

root.mainloop()
