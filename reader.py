import os
from Klasse import Klasse


class Reader:
    def __init__(self, path):
        self.path = path
        self.uml_klassen = []
        self.classnames = []
        self.set_classnames()
        self.set_uml_klassen_list()

    def set_uml_klassen_list(self):
        for filename in os.listdir(self.path):
            if ".java" in filename:
                self.uml_klassen.append(self.get_uml_klasse(filename))

    def set_classnames(self):
        for filename in os.listdir(self.path):
            if ".java" in filename:
                self.classnames.append(filename.split(".")[0])

    def get_uml_klasse(self, filename):
        variables = []
        methods = []
        reference_names = []
        motherclass = ""
        with open(self.path + filename, "r") as file:
            for line in file:
                if "private" in line or "public" in line:
                    # print(line, filename.split(".")[0] in line)
                    if "class" not in line and filename.split(".")[0] not in line:
                        if "(" in line:
                            methods.append(self.strip_method(line))
                        else:
                            variables.append(self.strip_variable(line))
                        reference_names.extend(self.get_reference_names(line))
                    elif " extends " in line:
                        motherclass = line.split(" extends ")[1].split(" ")[0].strip()
        return Klasse(filename.split(".")[0], methods, variables, list(set(reference_names)), motherclass)

    def get_reference_names(self, line):
        return [x for x in self.classnames if x in line]

    def strip_method(self, methodname):
        new_methodname = methodname.strip()
        new_methodname = self.replace_visibility_indicator(new_methodname)
        new_methodname_without_parameters = new_methodname.split("(")[0] + "( "
        parameters = new_methodname.split("(")[1].replace(")", "").split(",")
        for parameter in parameters:
            new_methodname_without_parameters += self.strip_parameter(parameter) + " "
        return new_methodname_without_parameters + ")"

    def strip_variable(self, variablename):
        new_variablename = variablename.strip().split(";")[0].split(" ")
        new_variablename[1], new_variablename[2] = new_variablename[2], new_variablename[1]
        new_variablename = " ".join(new_variablename)
        new_variablename = self.replace_visibility_indicator(new_variablename).replace(" ", " : ")
        return new_variablename

    def replace_visibility_indicator(self, indicator):
        return indicator.replace("private ", "-").replace("public ", "+").replace("protected ", "#").replace("package ",
                                                                                                             "~")
    def strip_parameter(self, parameter):
        parameter = parameter.split(" ")
        parameter[0], parameter[1] = parameter[1], parameter[0]
        return " : ".join(parameter)
