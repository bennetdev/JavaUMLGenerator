# Underlying logic to save all important information of the read java-class
class Klasse:
    def __init__(self, name, methods, variables, reference_names, motherclass):
        self.name = name
        self.motherclass = motherclass
        self.methods = methods
        self.variables = variables
        self.reference_names = reference_names
