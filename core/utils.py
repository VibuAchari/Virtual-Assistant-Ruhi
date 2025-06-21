# core/utils.py

import datetime
import random
import pyttsx3
import pyjokes
import os
import webbrowser
from core import voice
from tkinter import Tk, Entry, Label, Button, StringVar

app_paths = {
    "zoom": r"C:\\Users\\Admin\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe",
    "command prompt": r"C:\\Windows\\system32\\cmd.exe",
    "excel": r"C:\\Program Files\\Microsoft Office\\root\\Office16\\EXCEL.EXE",
    "powerpoint": r"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    "word": r"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "access": r"C:\\Program Files\\Microsoft Office\\root\\Office16\\MSACCESS.EXE",
    "chrome": r"C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe",
    "paint": r"C:\\Windows\\system32\\mspaint.exe",
    "vscode": r"C:\\Users\\Admin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "spotify": r"C:\\Users\\Admin\\AppData\\Roaming\\Spotify\\Spotify.exe",
    "mysql": r"C:\\Program Files\\MySQL\\MySQL Server 5.5\\bin\\mysql.exe"
}

def handle_app_launch(app_name, say):
    app_name = app_name.strip().lower()
    say(f"Opening {app_name}")
    path = app_paths.get(app_name)
    if path and os.path.exists(path):
        os.startfile(path)
    else:
        webbrowser.open(f"https://www.{app_name.replace(' ', '')}.com")

def calculate_expression(expr):
    try:
        return str(eval(expr))
    except:
        return "Sorry, I couldn't calculate that."

def pic_prompt():
    return random.choice(["Say cheese!", "Smile please!"])

def take_time():
    return datetime.datetime.now().strftime("%I:%M %p")

def take_date():
    return datetime.datetime.now().strftime("%B %d, %Y")

def wish_user(user):
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"
    voice.speak(f"{greeting} {user}. How can I help you?")

def get_battery_status():
    from plyer import battery
    state = battery.get_state()
    return f"Battery is at {state['percentage']}%"

def warn_if_low_battery(say):
    from plyer import battery
    state = battery.get_state()
    if state['percentage'] < 20 and not state['isCharging']:
        say("Battery is low. Please plug in the charger.")

def change_name_prompt():
    from core import database

    def changed():
        nm = name_var.get()
        database.change_username(nm)
        voice.speak("Name changed. Will reflect on next restart.")
        window.destroy()

    window = Tk()
    window.title("Change Name")
    window.geometry("400x300")
    window.configure(bg="black")
    window.wm_iconbitmap('resources/winlogo.ico')

    name_var = StringVar()
    Label(window, text="New name:", fg="white", bg="black").place(relx=.4, rely=.3, anchor="center")
    Entry(window, textvariable=name_var).place(relx=.7, rely=.3, anchor="center")
    Button(window, text="Submit", command=changed, bg="#15E546").place(relx=.5, rely=.7, anchor="center")
    window.mainloop()
