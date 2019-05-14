
from Objects.varObject import VariableObject

class Parser(object):
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_index = 0
        self.transpiled_code = ""

    def parse(self):
        while self.token_index < len(self.tokens):

            #holds the type of token
            token_type = self.tokens[self.token_index][0]

            #holds the value of the token
            token_value = self.tokens[self.token_index][1]

            if token_type == "VAR_DECLARATION" and token_value == "var":
                self.parse_variable_declaration(self.tokens[self.token_index:len(self.tokens)])

            #iterate token index by 1 to iterate through tokens
            self.token_index += 1

        print(self.transpiled_code)

    def parse_variable_declaration(self, token_stream):

        tokens_checked = 0

        name = ""
        operator = ""
        value = ""

        for token in range(0, len(token_stream)):
            token_type = token_stream[tokens_checked][0]
            token_value = token_stream[tokens_checked][1]

            #If the statement end is found it breaks out
            if token_type == "STATEMENT_END":
                break

            #this will get the variable name
            elif token == 1 and token_type == "IDENTIFIER":
                name = token_value

            #this will do error validation for invalid variable names
            elif token == 1 and token_type != "IDENTIFIER":
                print("Error: Invalid variable name '" + token_value +  "'")
                quit()

            #this will get the variable assignment operator
            elif token == 2 and token_type == "OPERATOR":
                operator = token_value
            elif token == 2 and token_type != "OPERATOR":
                print("Error: Assignment operator is missing or invalid " )
                quit()

            #this will get the variable value assigned
            elif token == 3 and token_type in ['STRING', 'INTEGER', 'IDENTIFIER']:
                value = token_value
            elif token == 3 and token_type not in ['STRING', 'INTEGER', 'IDENTIFIER']:
                print("Error: Invalid variable assignment value '" + token_value + "'")
                quit()

            tokens_checked += 1

        varObj = VariableObject()
        self.transpiled_code += varObj.transpile(name, operator, value )

        #increment token index by amount of tokens checked so we dont check again
        self.token_index += tokens_checked