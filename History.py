import tkinter as tk
from tkinter import Toplevel, Label, Text, Button, END

class HistoryClass:
    def __init__(self, master):
        self.master = master
        self.master.title("Action History")
        self.master.geometry("400x400")
        self.master.withdraw()  # Start hidden

        # Text widget to display history
        self.history_text = Text(self.master, wrap='word')
        self.history_text.pack(expand=True, fill='both')

        # Button to close the history window
        close_button = Button(self.master, text="Close", command=self.master.withdraw)
        close_button.place(y="420", width="12",height="10", )

        self.load_history()  # Load history on initialization

    def log_action(self, action):
        self.history_text.insert(END, action + '\n')
        self.history_text.see(END)  # Scroll to the bottom
        self.save_history(action)

    def load_history(self):
        try:
            with open("C:\\Users\\MyPC\\Pictures\\New folder\\PROJECT 1-20241005T115651Z-001\\PROJECT 1\\Data\\history.txt", "r") as file:
                for line in file:
                    self.history_text.insert(END, line)
        except FileNotFoundError:
            print("History file not found. Starting with an empty history.")

    def save_history(self, action):
        with open("C:\\Users\\MyPC\\Pictures\\New folder\\PROJECT 1-20241005T115651Z-001\\PROJECT 1\\Data\\history.txt", "a") as file:
            file.write(action + '\n')
