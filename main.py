# main.py

from tkinter import Tk
from ui.splash import SplashScreen
from ui.interface import MainRoot

def destroy_splash_and_start_main():
    global splash
    try:
        if splash.winfo_exists():
              splash.destroy()
    except Exception as e:
        print(f"[Warning] Splash destroy failed: {e}")
    MainRoot()

if __name__ == '__main__':
    splash = Tk()
    splash.overrideredirect(True)
    SplashScreen(splash)
    splash.after(4000, destroy_splash_and_start_main)  # ✅ No lambda used
    splash.mainloop()
