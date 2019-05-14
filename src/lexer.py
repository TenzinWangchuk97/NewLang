import re

class Lexer(object):
    def __init__(self, source_code):
        self.source_code = source_code

    def tokenize(self):

        #where tokens are stored
        tokens = []

        #list of words of source code
        source_code = self.source_code.split()

        #keeps track of word index
        source_index = 0

        #loop to pass each word in source code
        while source_index < len(source_code):

            word =source_code[source_index]

            if word == "var":
                tokens.append(["VAR_DECLARATION", word])

            #recognizes words and creates indentifier token for it
            elif re.match('[a-z]',word) or re.match('[A-Z]', word):
                #removes semicolon from end of words
                if word[len(word) - 1 ] == ";":
                    tokens.append(['IDENTIFIER', word[0:len(word)-1]])
                else:
                    tokens.append(['IDENTIFIER', word])

            #recognizes integers and creates integer token for it
            elif re.match('[0-9]', word):
                #removes semicolon from end of integers
                if word[len(word) - 1] == ";":
                    tokens.append(['INTEGER', word[0:len(word)-1]])
                else:
                    tokens.append(['INTEGER', word])

            #recognizes individual operators and creates operator token for it
            elif re.match('[-+=/*]', word):
                if len(word) > 1:
                    for x in range(len(word)):
                        tokens.append(['OPERATOR', word[x]])
                else:
                    tokens.append(['OPERATOR', word])

            #recognizes left parenthesis and creates left token for it
            elif re.match('[(]', word):
                tokens.append(['L_PARENTH', word])

            #recognizes right parenthesis and creates right token for it
            elif re.match('[)]', word):
                tokens.append(['R_PARENTH', word])

            #recognizes if last character in a word a is semicolon and creates statement end token
            if word[len(word) - 1] == ";":
                tokens.append(['STATEMENT_END', ';'])

            source_index += 1

        print(tokens)

        #returns created tokens
        return tokens
