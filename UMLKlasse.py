import tkinter as tk
from tkinter import font as tkFont


# Canvas of one class in the UML-Chart
class UMLKlasse(tk.Canvas):
    def __init__(self, klasse, canvas):
        self.klasse = klasse
        self.drawed = []
        self.references = []
        self.window = None
        self.x = 0
        self.y = 0
        self.motherclass = None
        self.width = self.get_min_canvas_width()
        self.height = self.get_min_canvas_height()
        # init own canvas with right dimensions and remove edges
        tk.Canvas.__init__(self, master=canvas, width=self.width + 1, height=self.height + 1, bg="#ffffff",
                           bd=0,
                           relief="ridge",
                           highlightthickness=0)

    # get the needed canvas width to display every element
    def get_min_canvas_width(self):
        font = tkFont.Font(family="Purisa", size=9)
        # get all text displayed in this canvas
        all_displayed_text = self.klasse.methods.copy()
        all_displayed_text.extend(self.klasse.variables)
        # get pixel width of longest text or set standard value of 100
        return max([font.measure(text) for text in all_displayed_text]) + 3 if all_displayed_text else 100

    # get the needed canvas height to display every element
    def get_min_canvas_height(self):
        # calculate by number of methods and variables
        height = 25 + ((10 + 15 * (len(self.klasse.variables) - 1)) if len(self.klasse.variables) > 0 else 0) + (
            (20 + 15 * (len(self.klasse.methods) - 1)) if len(self.klasse.methods) > 0 else 0) + 10
        return height

    # draw the UML-Box for this class
    def create_single_class_rect(self):
        self.create_text(2, 0, anchor="nw", font=("Purisa", 9), text=self.klasse.name)
        self.create_line(0, 25, self.width, 25)
        # value for start of line separating variables and methods
        separator_y = 0
        # iterate over variable-names in current class
        for variable_index, variable_name in enumerate(self.klasse.variables):
            separator_y = 35 + 15 * variable_index
            self.create_text(2, separator_y, font=("Purisa", 9), text=variable_name, anchor="w")
        # generate sepator line if there are variables
        if separator_y != 0:
            self.create_line(0, separator_y + 10, self.width, separator_y + 10)
        rectangle_end_y = separator_y
        # iterate over method-names in current class
        for method_index, method_name in enumerate(self.klasse.methods):
            rectangle_end_y = (separator_y + 20) + 15 * method_index + (15 if separator_y == 0 else 0)
            # print(rectangle_end_y)
            self.create_text(2, rectangle_end_y, font=("Purisa", 9), text=method_name, anchor="w")
        # create rectangle for class in specific size
        self.create_rectangle(0, 0, self.width, rectangle_end_y + 10)

    # save the position on parent canvas saved in GUI.py
    def set_position(self, x, y):
        self.x = x
        self.y = y

    # get position of nearest snapping point to x, y for reference arrows
    def get_nearest_center_pos(self, x, y):
        # calculate position of snapping points by current position of center and height and width
        left = (self.x - self.width / 2, self.get_center_y())
        top = (self.get_center_x(), self.y + self.height / 2)
        right = (self.x + self.width / 2, self.get_center_y())
        bottom = (self.get_center_x(), self.y - self.height / 2)
        # add to one list and create list of distances to x, y by use pythagorean theorem
        centers = [left, top, right, bottom]
        distances = [abs(x - side_x) ** 2 + abs(side_y - y) ** 2 for side_x, side_y in centers]
        # return position (tupel of x, y) of the nearest snapping point
        return centers[distances.index(min(distances))]

    # get x-position of center on parent canvas (currently just x-coordinate because of anchor="center")
    def get_center_x(self):
        return self.x

    # get y-position of center on parent canvas (currently just y-coordinate because of anchor="center")
    def get_center_y(self):
        return self.y
