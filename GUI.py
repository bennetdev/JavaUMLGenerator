import tkinter as tk
from tkinter import *
from tkinter import filedialog
import sys
import threading
from UMLKlasse import UMLKlasse
from Klasse import Klasse
from math import sqrt
from reader import Reader


class View:
    def __init__(self, master, width, height):
        self.width = width
        self.height = height
        self.master = master
        self.bar_height = 100
        self.display_size_index = -1
        self.uml_to_drag = None
        self.uml_klassen = []
        self.reference_arrows = []
        self.reader = Reader("C:\\Users\\Bennet\\Desktop\\Java\\Projekte\\NetwerkTest\\")
        master.title("UML Generator")
        self.master.resizable(False, False)
        self.frame = tk.Frame(self.master, width=width, height=height)
        self.frame.pack(expand=True, fill="both")
        self.canvas = tk.Canvas(self.frame, width=1200, height=800, bg="#ffffff")
        self.canvas.pack()
        self.master.bind("<ButtonPress-1>", self.drag_start)
        self.master.bind("<ButtonRelease-1>", self.drag_release)
        self.display_all_umls()
        self.create_references()
        self.draw_all_reference_arrows()

    def display_all_umls(self):
        for index, uml in enumerate(self.reader.uml_klassen):
            uml_klasse = UMLKlasse(uml, self.canvas)
            self.uml_klassen.append(uml_klasse)
            self.display_uml(uml_klasse, 250 * index,150+ 250 * (index // 5))

    def display_uml(self, uml, x, y):
        uml.set_position(x, y)
        uml.pack()
        uml_window = self.canvas.create_window(x, y, anchor="center", window=uml)
        uml.create_single_class_rect()

    def move_uml_klasse(self, uml, x, y):
        self.canvas.create_window(x, y, anchor="center", window=uml)
        uml.set_position(x, y)

    def drag_release(self, event):
        print(event.x, event.y)
        x = self.master.winfo_pointerx() - self.master.winfo_rootx()
        y = self.master.winfo_pointery() - self.master.winfo_rooty()
        self.move_uml_klasse(self.uml_to_drag, x, y)
        self.draw_all_reference_arrows()

    def drag_start(self, event):
        x = self.master.winfo_pointerx() - self.master.winfo_rootx()
        y = self.master.winfo_pointery() - self.master.winfo_rooty()
        self.uml_to_drag = self.get_nearest_uml(x, y)
        print(self.uml_to_drag, event.x, event.y, x, y)

    def get_nearest_uml(self, x, y):
        sorted_uml = sorted(self.uml_klassen, key=lambda uml: sqrt(abs(uml.x - x) ** 2 + abs(uml.y - y) ** 2))
        return sorted_uml[0]

    def draw_all_reference_arrows(self):
        for arrow in self.reference_arrows:
            self.canvas.delete(arrow)
        for uml_klasse in self.uml_klassen:
            for reference_uml in uml_klasse.references:
                self.draw_reference_arrow(uml_klasse, reference_uml)

    def draw_reference_arrow(self, uml_klasse1, uml_klasse2):
        x2, y2 = uml_klasse2.get_nearest_center_pos(uml_klasse1.x, uml_klasse1.get_center_y())
        print(uml_klasse2.klasse.name, x2, y2)
        self.reference_arrows.append(
            self.canvas.create_line(uml_klasse1.x, uml_klasse1.get_center_y(), x2, y2, dash=(2, 1), arrow=tk.LAST))

    def create_references(self):
        for uml_klasse in self.uml_klassen:
            for uml_klasse2 in self.uml_klassen:
                if uml_klasse2.klasse.name in uml_klasse.klasse.reference_names:
                    uml_klasse.references.append(uml_klasse2)


root = tk.Tk()
view = View(root, 400, 400)
root.mainloop()
