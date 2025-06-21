# ui/test_mic.py

from tkinter import Toplevel, Label, Button
from core import voice

class MicTester:
    def __init__(self, parent=None):
        self.window = Toplevel(parent)
        self.window.title("Test Microphone")
        self.window.geometry("500x300")
        self.window.configure(bg="black")

        Label(self.window, text="🎤 Test your microphone",
              font=("Segoe UI", 18, "bold"), fg="white", bg="black").pack(pady=20)

        self.result_label = Label(self.window, text="(Press the button and speak)",
                                  font=("Segoe UI", 14), fg="white", bg="black")
        self.result_label.pack(pady=10)

        Button(self.window, text="Start Mic Test", font=("Segoe UI", 12, "bold"),
               bg="#013f5a", fg="white", activebackground="#013f5a",
               command=self.run_test).pack(pady=20)

    def run_test(self):
        query = voice.listen()
        if query:
            self.result_label.config(text=f"You said: {query}")
            voice.speak(f"You said: {query}")
        else:
            self.result_label.config(text="Sorry, I couldn't hear you.")
