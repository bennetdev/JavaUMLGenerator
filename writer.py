from fpdf import FPDF
from math import floor

# Class to save uml as PDF (Under development, not finished)
class Writer:
    def __init__(self, classes):
        self.classes = classes
        self.pdf = FPDF(orientation="L")

    # create pdf
    def write_to_pdf(self):
        self.pdf.add_page()
        self.pdf.set_font("Arial", size=12)
        self.create_class_rects()
        self.pdf.output("uml.pdf")

    # Create rectangles + content for UML-Diagram
    def create_class_rects(self):
        # iterate over classes dictionary
        for class_index, class_item in enumerate(self.classes):
            offset_x = 110 * (0 if class_index == 0 else class_index % 2)
            offset_y = floor(100 * (class_index // 2))
            print(offset_y)
            self.create_single_class_rect(offset_x, offset_y, class_item)


    def create_single_class_rect(self, offset_x, offset_y, class_item):
        self.pdf.text(55 + offset_x, 20 + offset_y, txt=class_item)
        self.pdf.line(10 + offset_x, 25 + offset_y, 110 + offset_x, 25 + offset_y)
        # value for start of line separating variables and methods
        separator_y = 0
        # iterate over variable-names in current class
        for variable_index, variable_name in enumerate(self.classes[class_item]["variables"]):
            separator_y = 35 + 5 * variable_index
            self.pdf.text(20 + offset_x, separator_y + offset_y, txt=variable_name)
        # generate sepator line if there are variables
        if separator_y != 0:
            self.pdf.line(10 + offset_x, separator_y + 5 + offset_y, 110 + offset_x, separator_y + 5 + offset_y)
        rectangle_end_y = separator_y
        # iterate over method-names in current class
        for method_index, method_name in enumerate(self.classes[class_item]["methods"]):
            rectangle_end_y = (separator_y + 15) + 5 * method_index
            self.pdf.text(20 + offset_x, rectangle_end_y + offset_y, txt=method_name)
        # create rectangle for class in specific size
        self.pdf.rect(10 + offset_x, 10 + offset_y, 100, rectangle_end_y - 5)
