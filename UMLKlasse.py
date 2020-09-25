import tkinter as tk


class UMLKlasse(tk.Canvas):
    def __init__(self, klasse, canvas):
        tk.Canvas.__init__(canvas, width=100, height=200)
        self.klasse = klasse
        self.drawed = []

    def delete_drawed(self):
        for drawed in self.drawed:
            self.canvas.delete(drawed)

    def draw(self):
        pass

    def create_single_class_rect(self, offset_x, offset_y):
        self.drawed.append(self.canvas.create_text(55 + offset_x, 20 + offset_y, text=self.klasse.name))
        self.drawed.append(self.canvas.create_line(10 + offset_x, 25 + offset_y, 150 + offset_x, 25 + offset_y))
        # value for start of line separating variables and methods
        separator_y = 0
        # iterate over variable-names in current class
        for variable_index, variable_name in enumerate(self.klasse.variables):
            separator_y = 35 + 15 * variable_index
            self.drawed.append(self.canvas.create_text(20 + offset_x, separator_y + offset_y, text=variable_name, anchor="w"))
        # generate sepator line if there are variables
        if separator_y != 0:
            self.drawed.append(self.canvas.create_line(10 + offset_x, separator_y + 10 + offset_y, 150 + offset_x,
                                    separator_y + 10 + offset_y))
        rectangle_end_y = separator_y
        # iterate over method-names in current class
        for method_index, method_name in enumerate(self.klasse.methods):
            rectangle_end_y = (separator_y + 20) + 15 * method_index
            print(rectangle_end_y)
            self.drawed.append(self.canvas.create_text(20 + offset_x, rectangle_end_y + offset_y, text=method_name, anchor="w"))
        # create rectangle for class in specific size
        self.drawed.append(self.canvas.create_rectangle(10 + offset_x, 10 + offset_y, 150 + offset_x,
                                                        rectangle_end_y + offset_y + 10))
