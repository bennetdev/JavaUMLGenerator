import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sys
import threading
from UMLKlasse import UMLKlasse
from Klasse import Klasse


class View:
    def __init__(self, master, width, height):
        self.width = width
        self.height = height
        self.master = master
        self.bar_height = 100
        self.display_size_index = -1

        master.title("UML Generator")
        self.frame = tk.Frame(self.master, width=width, height=height)
        self.frame.pack(expand=True)
        self.canvas = tk.Canvas(self.frame, width=400, height=400, bg="#ffffff")
        self.canvas.pack()

        uml = UMLKlasse(
            Klasse("Klasse1", ["String method5", "void method6"], ["String var5", "int var6", "double var7"]),
            self.frame)

        uml.pack()
        uml_window = self.canvas.create_window(100,100,anchor="nw",window=uml)
        uml.create_single_class_rect(200, 100)

        uml = UMLKlasse(
            Klasse("Klasse2", ["String method5", "void method6"], ["String var5", "int var6", "double var7"]),
            self.master)
        uml_window = self.canvas.create_window(100, 300, anchor="nw", window=uml)
        uml.create_single_class_rect(200, 100)


root = tk.Tk()
view = View(root, 400, 400)
root.mainloop()
