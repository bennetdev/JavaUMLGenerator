import tkinter as tk


class UMLKlasse(tk.Canvas):
    def __init__(self, klasse, canvas):
        tk.Canvas.__init__(self, master=canvas, width=151, height=200, bg="#ffffff", bd=0, relief="ridge",
                           highlightthickness=0)
        self.klasse = klasse
        self.drawed = []

    def delete_drawed(self):
        for drawed in self.drawed:
            self.delete(drawed)

    def draw(self):
        pass

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
            print(rectangle_end_y)
            self.create_text(2, rectangle_end_y, text=method_name, anchor="w")
        # create rectangle for class in specific size
        self.create_rectangle(0, 0, 150, rectangle_end_y + 10)
