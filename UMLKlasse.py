
class UMLKlasse:
    def __init__(self, class_dictionary, canvas, classname):
        self.class_dictionary = class_dictionary
        self.canvas = canvas
        self.classname = classname

    def draw(self):
        pass
    def create_single_class_rect(self, offset_x, offset_y):
        self.canvas.create_text(55 + offset_x, 20 + offset_y, text=self.classname)
        self.canvas.create_line(10 + offset_x, 25 + offset_y, 110 + offset_x, 25 + offset_y)
        # value for start of line separating variables and methods
        separator_y = 0
        # iterate over variable-names in current class
        for variable_index, variable_name in enumerate(self.class_dictionary["variables"]):
            separator_y = 35 + 5 * variable_index
            self.canvas.create_text(20 + offset_x, separator_y + offset_y, text=variable_name)
        # generate sepator line if there are variables
        if separator_y != 0:
            self.canvas.create_line(10 + offset_x, separator_y + 5 + offset_y, 110 + offset_x, separator_y + 5 + offset_y)
        rectangle_end_y = separator_y
        # iterate over method-names in current class
        for method_index, method_name in enumerate(self.class_dictionary["methods"]):
            rectangle_end_y = (separator_y + 15) + 5 * method_index
            self.canvas.create_text(20 + offset_x, rectangle_end_y + offset_y, text=method_name)
        # create rectangle for class in specific size
        self.canvas.create_rectangle(10 + offset_x, 10 + offset_y, 100, rectangle_end_y - 5)