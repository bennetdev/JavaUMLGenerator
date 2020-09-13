from fpdf import FPDF


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
            offset = 110 * class_index
            self.create_single_class_rect(offset, class_item)

    def create_single_class_rect(self, offset, class_item):
        self.pdf.text(55 + offset, 20, txt=class_item)
        self.pdf.line(10 + offset, 25, 110 + offset, 25)
        # value for start of line separating variables and methods
        separator_y = 0
        # iterate over variable-names in current class
        for variable_index, variable_name in enumerate(self.classes[class_item]["variables"]):
            separator_y = 35 + 5 * variable_index
            self.pdf.text(20 + offset, separator_y, txt=variable_name)
        # generate sepator line if there are variables
        if separator_y != 0:
            self.pdf.line(10 + offset, separator_y + 5, 110 + offset, separator_y + 5)
        rectangle_end_y = separator_y
        # iterate over method-names in current class
        for method_index, method_name in enumerate(self.classes[class_item]["methods"]):
            rectangle_end_y = (separator_y + 15) + 5 * method_index
            self.pdf.text(20 + offset, rectangle_end_y, txt=method_name)
        # create rectangle for class in specific size
        self.pdf.rect(10 + offset, 10, 100, rectangle_end_y - 5)