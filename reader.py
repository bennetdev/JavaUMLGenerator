import os
from Klasse import Klasse


class Reader:
    def __init__(self, path):
        self.path = path
        self.uml_klassen = []
        self.set_uml_klassen_list()

    def set_uml_klassen_list(self):
        for filename in os.listdir(self.path):
            if ".java" in filename:
                self.uml_klassen.append(self.get_uml_klasse(filename))

    def get_uml_klasse(self, filename):
        variables = []
        methods = []
        with open(self.path + filename, "r") as file:
            for line in file:
                if "private" in line or "public" in line:
                    print(line, filename.split(".")[0] in line)
                    if "class" not in line and filename.split(".")[0] not in line:
                        if "(" in line:
                            methods.append(self.strip_method(line))
                        else:
                            variables.append(self.strip_variable(line))
        return Klasse(filename.split("."), methods, variables)

    def strip_method(self, methodname):
        return methodname.strip().split("(")[0] + "()"
    def strip_variable(self, variablename):
        return variablename.strip().split(";")[0]
