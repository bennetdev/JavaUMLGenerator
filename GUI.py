import tkinter as tk
from UMLKlasse import UMLKlasse
from reader import Reader
from tkinter import filedialog


# Tkinter window to display whole UML-Chart
class View:
    def __init__(self, master):
        # span over full screen
        self.width = master.winfo_screenwidth()
        self.height = master.winfo_screenheight()
        self.master = master
        # save uml_klasse objects for interaction
        self.uml_to_drag = None
        self.uml_klassen = []
        self.reference_arrows = []
        self.inheritance_arrows = []
        # initialize reader with None for user to choose folder
        self.reader = None
        master.title("UML Generator")
        self.master.tk.call('wm', 'iconphoto', master._w, tk.PhotoImage(file='rsc/icon.png'))
        self.master.resizable(False, False)
        self.frame = tk.Frame(self.master, width=self.width, height=self.height)
        self.frame.pack(expand=True, fill="both")
        self.canvas = tk.Canvas(self.frame, width=self.width, height=self.height, bg="#ffffff")
        self.canvas.pack()
        # add menu bar
        self.menu = tk.Menu(self.master)
        self.menu.add_command(label="Pick Folder", command=self.pick_folder)
        self.master.config(menu=self.menu)

    # create all umls and add drag feature
    def start(self):
        self.master.bind("<ButtonPress-1>", self.drag_start)
        self.master.bind("<ButtonRelease-1>", self.drag_release)
        self.display_all_umls()
        self.create_references()
        self.draw_all_reference_arrows()

    # pick folder with filedialog
    def pick_folder(self):
        f = filedialog.askdirectory()
        # if a folder is chosen (not the case e.g. if canceled)
        if f != "":
            self.reader = Reader(f + "/")
            self.start()

    # display all umls for the first time
    def display_all_umls(self):
        row = 1
        current_width = 0
        min_row_height = 0
        current_height = 100
        for index, uml in enumerate(self.reader.uml_klassen):
            print(current_width, self.width)
            uml_klasse = UMLKlasse(uml, self.canvas)
            print("w", uml_klasse.width)
            if current_width + uml_klasse.width > self.width:
                row += 1
                current_width = 0
                current_height += min_row_height
                min_row_height = 0
            current_width += uml_klasse.width / 2
            self.uml_klassen.append(uml_klasse)
            self.display_uml(uml_klasse, current_width, current_height)
            current_width += uml_klasse.width / 2 + 2
            if uml_klasse.height > min_row_height:
                min_row_height = uml_klasse.height

    # display uml_klasse on position x,y
    def display_uml(self, uml, x, y):
        uml.pack()
        # create window on this canvas
        self.move_uml_klasse(uml, x, y)
        # create box on the canvas of the uml
        uml.create_single_class_rect()

    # move uml_klasse to position x,y
    def move_uml_klasse(self, uml, x, y):
        self.canvas.create_window(x, y, anchor="center", window=uml)
        uml.set_position(x, y)

    # trigger on ending drag
    def drag_release(self, event):
        x = self.master.winfo_pointerx() - self.master.winfo_rootx()
        y = self.master.winfo_pointery() - self.master.winfo_rooty()
        # release saved uml_klasse in uml_to_drag
        self.move_uml_klasse(self.uml_to_drag, x, y)
        self.draw_all_reference_arrows()

    # trigger on starting drag
    def drag_start(self, event):
        x = self.master.winfo_pointerx() - self.master.winfo_rootx()
        y = self.master.winfo_pointery() - self.master.winfo_rooty()
        # get nearest uml and save it (as the one to be moved at release)
        self.uml_to_drag = self.get_nearest_uml(x, y)

    # get nearest uml_klasse by x, y
    def get_nearest_uml(self, x, y):
        # get nearest uml_klasse by pythagorean theorem
        sorted_uml = sorted(self.uml_klassen, key=lambda uml: abs(uml.x - x) ** 2 + abs(uml.y - y) ** 2)
        return sorted_uml[0]

    # draw all inheritance and reference arrows
    def draw_all_reference_arrows(self):
        # delete current displayed arrows
        for arrow in self.reference_arrows:
            self.canvas.delete(arrow)
        for arrow in self.inheritance_arrows:
            self.canvas.delete(arrow)
        for uml_klasse in self.uml_klassen:
            for reference_uml in uml_klasse.references:
                self.draw_reference_arrow(uml_klasse, reference_uml)
            if uml_klasse.motherclass is not None:
                self.draw_inheritance_arrow(uml_klasse, uml_klasse.motherclass)

    # draw reference arrow from uml_klasse_from to uml_klasse_to
    def draw_reference_arrow(self, uml_klasse_from, uml_klasse_to):
        # get coords of nearest snapping point of uml_klasse_to
        x2, y2 = uml_klasse_to.get_nearest_center_pos(uml_klasse_from.x, uml_klasse_from.get_center_y())
        print(uml_klasse_to.klasse.name, x2, y2)
        # save to delete on new creation
        self.reference_arrows.append(
            self.canvas.create_line(uml_klasse_from.x, uml_klasse_from.get_center_y(), x2, y2, dash=(2, 1),
                                    arrow=tk.LAST))

    # draw inheritance arrow from uml_klasse_from to uml_klasse_to
    def draw_inheritance_arrow(self, uml_klasse_from, uml_klasse_to):
        # get coords of nearest snapping point of uml_klasse_to
        x2, y2 = uml_klasse_to.get_nearest_center_pos(uml_klasse_from.x, uml_klasse_from.get_center_y())
        print(uml_klasse_to.klasse.name, x2, y2)
        # save to delete on new creation
        self.inheritance_arrows.append(
            self.canvas.create_line(uml_klasse_from.x, uml_klasse_from.get_center_y(), x2, y2, arrow=tk.LAST))

    # create references and inheritance by saved classnames
    def create_references(self):
        for uml_klasse in self.uml_klassen:
            for uml_klasse2 in self.uml_klassen:
                # check if the name of uml_klasse2 is in references of uml_klassen1 or the motherclass
                if uml_klasse2.klasse.name in uml_klasse.klasse.reference_names:
                    # save in current class
                    uml_klasse.references.append(uml_klasse2)
                if uml_klasse2.klasse.name == uml_klasse.klasse.motherclass:
                    # save in current class
                    uml_klasse.motherclass = uml_klasse2



