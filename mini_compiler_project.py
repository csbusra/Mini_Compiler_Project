class LexicalAnalyzer:
    def __init__(self, code):
        # Initialize the Lexeical Analyzer with the input text and set the initial position to 0
        self.code = code
        self.position = 0
        self.tokens = []
        self.generate_tokens()

    def generate_tokens(self):
        #traverse the code character by character
        while self.position < len(self.code):
            current_char = self.code[self.position]
            if current_char.isdigit():
                # If the current character is a digit, return a NUMBER token
                self.position += 1
                self.tokens.append(("NUMBER", int(current_char)))
            elif current_char == '+':
                # If the current character is '+', return a PLUS token
                self.position += 1
                self.tokens.append(("PLUS", current_char))
            elif current_char == '-':
                # If the current character is '-', return a MINUS token
                self.position += 1
                self.tokens.append(("MINUS", current_char))
            elif current_char == '*':
                # If the current character is '+', return a PLUS token
                self.position += 1
                self.tokens.append(("MUL", current_char))
            elif current_char == '/':
                # If the current character is '-', return a MINUS token
                self.position += 1
                self.tokens.append(("DIV", current_char))
            elif current_char.isspace():
                # Ignore whitespace characters
                self.position += 1
                continue
            else:
                raise SyntaxError("Character not recognised: {}".format(current_char))

        # Return EOF (end-of-file) when the end of the input is reached
        self.tokens.append(("EOF", None))

class Node:
    def __init__(self, value, children=None):
        self.value = value
        self.children = children or []
     
class SynatxAnalyzer:
    def __init__(self, tokens):
        # Initialize the Parser with a lexer and set the current token to None
        self.tokens = tokens
        self.current_token = None
        self.current_position = 0
    
    def analyze(self):
        self.current_token = self.tokens[self.current_position]
        node = self.exp()
        if self.current_token[0] != "EOF":
            raise SyntaxError("Token not recognised: {}".format(self.current_token))
        return node
    
    # exp -> term + term | term - term | term
    def exp(self):
        # Parse and evaluate expressions
        node = self.term()
        while self.current_token[0] in ("PLUS", "MINUS"):
            operator = self.current_token[1]
            self.ahead(self.current_token[0])
            right_child = self.term()
            node = Node(operator, [node, right_child])
        return node

    #term -> fact * fact | fact / fact | fact
    def term(self):
        # Parse and evaluate expressions
        node = self.fact()
        while self.current_token[0] in ("MUL", "DIV"):
            operator = self.current_token[1]
            self.ahead(self.current_token[0])
            right_child = self.fact()
            node = Node(operator, [node, right_child])
        return node
    
    #fact -> NUMBER
    def fact(self):
        # Parse and evaluate terms
        if self.current_token[0] == "NUMBER":
            node = Node(self.current_token[1])
            self.ahead(self.current_token[0])
        else:
            raise SyntaxError("Token not recognised: {}".format(self.current_token))
        return node

    #khao r shamne zao
    def ahead(self, token_type):
        # Consume the current token if it matches the expected token type
        if self.current_token[0] in token_type:
            self.current_position += 1
            self.current_token = self.tokens[self.current_position]
        else:
            raise SyntaxError("Token not recognised: {}".format(self.current_token))

def print_syntax_tree(node, level=0):
    if node:
        print("  " * level + str(node.value))
        for child in node.children:
            print_syntax_tree(child, level + 1)     

def main():
    # Entry point of the program
    code = input()
    #phase 1: Lexical analyzer will generate tokens from the code
    lexicalAnalyzer = LexicalAnalyzer(code)
    print("The generated tokens are:")
    print(lexicalAnalyzer.tokens)
    print()
    syntaxAnalyzer = SynatxAnalyzer(lexicalAnalyzer.tokens)
    syntaxTree = syntaxAnalyzer.analyze()
    print("Program compiled without any syntax error...")
    print()
    print("Syntax Tree")
    print_syntax_tree(syntaxTree)


if __name__ == "__main__":
    # Run the main function if the script is executed
    main()