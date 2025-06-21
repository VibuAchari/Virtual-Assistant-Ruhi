# ui/splash.py

from tkinter import Tk, Canvas, BOTH
from PIL import Image, ImageTk, ImageSequence
import os

class SplashScreen:
    def __init__(self, parent):
        self.parent = parent
        gif_path = os.path.join('resources', 'log2.gif')
        self.gambar = Image.open(gif_path)
        imagew, imageh = self.gambar.size
        setscreenw = (self.parent.winfo_screenwidth() - imagew) // 2
        setscreenh = (self.parent.winfo_screenheight() - imageh) // 2
        self.parent.geometry(f"{imagew}x{imageh}+{setscreenw}+{setscreenh}")
        self.parent.configure(background="black")

        self.canvas = Canvas(self.parent, width=imagew, height=imageh)
        self.canvas.pack(fill=BOTH)

        self.sequence = [ImageTk.PhotoImage(img) for img in ImageSequence.Iterator(self.gambar)]
        self.image = self.canvas.create_image(400, 300, image=self.sequence[0])

        self.parent.after(4050, self.parent.destroy)
        self.animate(2)

    def animate(self, counter):
        self.canvas.itemconfig(self.image, image=self.sequence[counter])
        self.parent.after(20, lambda: self.animate((counter + 1) % len(self.sequence)))
