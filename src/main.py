import lexer
import parser

def main():
    content = ""
    with open('test.lang', 'r') as file:
        content = file.read()

    #lexer

    lex = lexer.Lexer(content)
    tokens =lex.tokenize()

    #parser

    parse = parser.Parser(tokens)
    parse.parse()
main()
