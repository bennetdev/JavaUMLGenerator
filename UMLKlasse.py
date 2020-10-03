import tkinter as tk


class UMLKlasse(tk.Canvas):
    def __init__(self, klasse, canvas):
        self.klasse = klasse
        self.drawed = []
        self.references = []
        self.window = None
        self.x = 0
        self.y = 0
        self.width = 151
        self.height = self.get_min_canvas_height()
        tk.Canvas.__init__(self, master=canvas, width=self.width, height=self.height+1, bg="#ffffff",
                           bd=0,
                           relief="ridge",
                           highlightthickness=0)

    def delete_drawed(self):
        for drawed in self.drawed:
            self.delete(drawed)

    def draw(self):
        pass

    def get_min_canvas_height(self):
        height = 25 + ((10 + 15 * (len(self.klasse.variables) - 1)) if len(self.klasse.variables) > 0 else 0) + (
            (20 + 15 * (len(self.klasse.methods) - 1)) if len(self.klasse.methods) > 0 else 0) + 10
        # print(self.klasse.name, height)
        return height

    def create_single_class_rect(self):
        self.create_text(2, 0, anchor="nw", text=self.klasse.name)
        self.create_line(0, 25, 150, 25)
        # value for start of line separating variables and methods
        separator_y = 0
        # iterate over variable-names in current class
        for variable_index, variable_name in enumerate(self.klasse.variables):
            separator_y = 35 + 15 * variable_index
            self.create_text(2, separator_y, text=variable_name, anchor="w")
        # generate sepator line if there are variables
        if separator_y != 0:
            self.create_line(0, separator_y + 10, 150, separator_y + 10)
        rectangle_end_y = separator_y
        # iterate over method-names in current class
        for method_index, method_name in enumerate(self.klasse.methods):
            rectangle_end_y = (separator_y + 20) + 15 * method_index
            # print(rectangle_end_y)
            self.create_text(2, rectangle_end_y, text=method_name, anchor="w")
        # create rectangle for class in specific size
        self.create_rectangle(0, 0, 150, rectangle_end_y + 10)

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def get_nearest_center_pos(self, x, y):
        left = (self.x - self.width / 2, self.get_center_y())
        top = (self.get_center_x(), self.y + self.height / 2)
        right = (self.x + self.width / 2, self.get_center_y())
        bottom = (self.get_center_x(), self.y - self.height / 2)
        centers = [left, top, right, bottom]
        distances = [abs(x-side_x) ** 2 + abs(side_y-y) ** 2 for side_x, side_y in centers]
        #print(self.klasse.name, centers)
        return centers[distances.index(min(distances))]

    def get_center_x(self):
        return self.x

    def get_center_y(self):
        return self.y
