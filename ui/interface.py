# ui/interface.py

from tkinter import Tk, Label, Button, PhotoImage
import os
from core import voice, database, logic
from ui.test_mic import MicTester
class MainRoot:
    def __init__(self):
        self.root = Tk()
        self.root.geometry('1280x800')
        self.root.wm_iconbitmap('resources/winlogo.ico')
        self.root.minsize(1280, 760)
        self.root.maxsize(1280, 760)
        self.root.configure(background="black")
        self.root.title("Ruhi - Virtual Assistant")

        # Background Image
        bg_img = PhotoImage(file="resources/bg.png", master=self.root)
        bg_label = Label(self.root, image=bg_img, bg="black", bd=0)
        bg_label.image = bg_img
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Microphone Button
        mic_img = PhotoImage(file="resources/micr.png", master=self.root)
        mic_button = Button(self.root, image=mic_img, command=self.start_mic,
                            bg="#000000", activebackground="#000000",
                            bd=0, highlightthickness=0)
        mic_button.image = mic_img
        mic_button.place(relx=.5, rely=.6, anchor="center")

        # History Button
        his_img = PhotoImage(file="resources/history.png", master=self.root)
        history_button = Button(self.root, image=his_img,
                                command=lambda: logic.output("history", "history"),
                                bg="#040f15", activebackground="#040f15",
                                bd=0, highlightthickness=0)
        history_button.image = his_img
        history_button.place(relx=.9, rely=.05, anchor="center")

        # Delete History Button
        del_img = PhotoImage(file="resources/del.png", master=self.root)
        delete_button = Button(self.root, image=del_img,
                               command=lambda: database.delete_history(),
                               bg="#040f15", activebackground="#040f15",
                               bd=0, highlightthickness=0)
        delete_button.image = del_img
        delete_button.place(relx=.97, rely=.05, anchor="center")

        # Welcome Message
        self.welcome_text = "HOW MAY I HELP YOU?"
        self.welcome_label = Label(self.root, text="",
                                   font=("Times New Roman", 36, "italic"),
                                   fg="white", bg="black", bd=0)
        self.welcome_label.place(relx=.5, rely=0.29, anchor="center")
        self.animate_welcome_text(0)

        self.root.mainloop()

    def animate_welcome_text(self, index):
        if index <= len(self.welcome_text):
            self.welcome_label.config(text=self.welcome_text[:index])
            self.root.after(70, lambda: self.animate_welcome_text(index + 1))

    def start_mic(self):
        query = voice.listen()
        if query:
            classified = logic.nlp.classify(query)
            logic.output(classified, query)
            
    def open_mic_tester(self):
        from core.voice import test_microphone
        test_microphone()