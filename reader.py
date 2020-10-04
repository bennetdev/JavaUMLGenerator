import os
from Klasse import Klasse


# Class to read java-classes from folder/files
class Reader:
    def __init__(self, path):
        self.path = path
        self.uml_klassen = []
        self.classnames = []
        self.set_classnames()
        self.set_uml_klassen_list()

    # generate uml-klasse for every file
    def set_uml_klassen_list(self):
        for filename in os.listdir(self.path):
            if ".java" in filename:
                self.uml_klassen.append(self.get_uml_klasse(filename))

    # save all classnames in list for references
    def set_classnames(self):
        for filename in os.listdir(self.path):
            if ".java" in filename:
                self.classnames.append(filename.split(".")[0])

    # generate uml-klasse from filename
    def get_uml_klasse(self, filename):
        variables = []
        methods = []
        reference_names = []
        motherclass = ""
        with open(self.path + filename, "r") as file:
            for line in file:
                # save objectvariables and methods
                if "private" in line or "public" in line:
                    # print(line, filename.split(".")[0] in line)
                    if "class" not in line and filename.split(".")[0] not in line:
                        if "(" in line:
                            methods.append(self.format_method(line))
                        else:
                            variables.append(self.format_variable(line))
                        # get all names of references to self defined classes
                        reference_names.extend(self.get_reference_names(line))
                    # save motherclass if class is extending other class
                    elif " extends " in line:
                        motherclass = line.split(" extends ")[1].split(" ")[0].strip()
        return Klasse(filename.split(".")[0], methods, variables, list(set(reference_names)), motherclass)

    # get names of all references made in line
    def get_reference_names(self, line):
        return [x for x in self.classnames if x in line]

    # format methodname for uml_klasse
    def format_method(self, methodname):
        new_methodname = methodname.strip()
        new_methodname = self.replace_visibility_indicator(new_methodname)
        # remove parantheses and parameters
        new_methodname_without_parameters = new_methodname.split("(")[0] + "( "
        # get list of parameters
        parameters = new_methodname.split("(")[1].replace(")", "").split(",")
        for parameter in parameters:
            # excluding cases like "{"
            if len(parameter) >= 3:
                # add formatted parameters back to methodname
                new_methodname_without_parameters += self.format_parameter(parameter) + " "
        return new_methodname_without_parameters + ")"

    # format variablename for uml_klasse
    def format_variable(self, variablename):
        new_variablename = variablename.strip().split(";")[0].split(" ")
        new_variablename[1], new_variablename[2] = new_variablename[2], new_variablename[1]
        new_variablename = " ".join(new_variablename)
        new_variablename = self.replace_visibility_indicator(new_variablename).replace(" ", " : ")
        return new_variablename

    # replace all visibility-are-indicators with the UML-indicators
    def replace_visibility_indicator(self, indicator):
        return indicator.replace("private ", "-").replace("public ", "+").replace("protected ", "#").replace("package ",
                                                                                                             "~")

    # format parametername for uml_klasse
    def format_parameter(self, parameter):
        parameter = parameter.split(" ")
        parameter[0], parameter[1] = parameter[1], parameter[0]
        return " : ".join(parameter)
