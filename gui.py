from tkinter import Tk, Label, Button
from worst_case_lottery import worst_case_lottery

class HockeyGUI:
    def __init__(self, master, message):
        self.master = master
        master.title("Hockey Info")
        master.geometry("400x50")

        self.label = Label(master, text = message)
        self.label.pack()

root = Tk()
message = worst_case_lottery()
my_gui = HockeyGUI(root, message)
root.mainloop()