import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sys
import threading
from UMLKlasse import UMLKlasse
from Klasse import Klasse
from math import sqrt


class View:
    def __init__(self, master, width, height):
        self.width = width
        self.height = height
        self.master = master
        self.bar_height = 100
        self.display_size_index = -1
        self.uml_to_drag = None
        self.uml_klassen = []

        master.title("UML Generator")
        self.frame = tk.Frame(self.master, width=width, height=height)
        self.frame.pack(expand=True, fill="both")
        self.canvas = tk.Canvas(self.frame, width=1200, height=800, bg="#ffffff")
        self.canvas.pack()
        self.master.bind("<ButtonPress-1>", self.drag_start)
        self.master.bind("<ButtonRelease-1>", self.drag_release)

        uml = UMLKlasse(
            Klasse("Klasse1", ["String method5", "void method6"], ["String var5", "int var6", "double var7"]),
            self.frame)
        self.uml_klassen.append(uml)
        self.display_uml(uml, 100, 100)
        uml = UMLKlasse(
            Klasse("Klasse2", ["String method5", "void method6"], ["String var5", "int var6", "double var7"]),
            self.frame)
        self.uml_klassen.append(uml)
        self.display_uml(uml, 300, 300)

    def display_uml(self, uml, x, y):
        uml.set_position(x, y)
        uml.pack()
        uml_window = self.canvas.create_window(x, y, anchor="nw", window=uml)
        uml.create_single_class_rect()

    def move_uml_klasse(self, uml, x, y):
        self.canvas.create_window(x, y, anchor="center", window=uml)
        uml.set_position(x, y)

    def drag_release(self, event):
        print(event.x, event.y)
        x = self.master.winfo_pointerx() - self.master.winfo_rootx()
        y = self.master.winfo_pointery() - self.master.winfo_rooty()
        self.move_uml_klasse(self.uml_to_drag, x, y)

    def drag_start(self, event):
        x = self.master.winfo_pointerx() - self.master.winfo_rootx()
        y = self.master.winfo_pointery() - self.master.winfo_rooty()
        self.uml_to_drag = self.get_nearest_uml(x, y)
        print(self.uml_to_drag, event.x, event.y, x, y)

    def get_nearest_uml(self, x, y):
        sorted_uml = sorted(self.uml_klassen, key=lambda uml: sqrt(abs(uml.x - x) ** 2 + abs(uml.y - y) ** 2))
        return sorted_uml[0]


root = tk.Tk()
view = View(root, 400, 400)
root.mainloop()
