import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sys
import threading

class View:
    def __init__(self, master, width, height):
        self.width = width
        self.height = height
        self.master = master
        self.bar_height = 100
        self.display_size_index = -1

        master.title("UML Generator")
        self.master.resizable(False, False)
        self.frame = tk.Frame(self.master, width=width, height=height)
        self.frame.pack(expand=True)
        self.canvas = tk.Canvas(self.frame, width=400, height=400, scrollregion=(0, 0, 0, 500), bg="#ffffff")
        self.canvas.pack()
        self.canvas.create_line(15, 25, 200, 25)



root = tk.Tk()
view = View(root, 400, 400)
root.mainloop()