
class VariableObject(object):

    def __init__(self):
        #holds python executable string for variable declaration
        self.exec_string = ""

    def transpile(self, name, operator, value):
        #appends the python executable string with parser
        self.exec_string += name + " " + operator + " " + value + "\n"
        return self.exec_string