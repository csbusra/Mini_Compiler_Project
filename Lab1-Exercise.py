from sys import stdin
from collections import defaultdict
# Set of keywords in C
keywords = {"auto", "break", "case", "char", "const", "continue", "default", "do", "double", "else", "enum", "extern", "float", "for", "goto", "if", "int", "long", "register", "return", "short", "signed", "sizeof", "static", "struct", "switch", "typedef", "union", "unsigned", "void", "volatile", "while"}

# Function to check if a string is a keyword or not
def is_keyword(word):
    return word in keywords

# Function to check if a string is an identifier or not
def is_identifier(word):
    if not word:
        return False
    if not word[0].isalpha() and word[0] != '_':
        return False
    for char in word[1:]:
        if not char.isalnum() and char != '_':
            return False
    return True

# Function to check if a string is a constant or not
def is_constant(word):
    if not word:
        return False
    return word.isdigit()

# Function to get the type of a token
def get_token_type(word):
    if is_keyword(word):
        return 'Keyword'
    elif is_identifier(word):
        return 'Identifier'
    elif is_constant(word):
        return 'Constant'
    else:
        return 'Invalid'

# Function to tokenize the input
tokens = defaultdict(set)
def tokenize(input):
    
    in_comment = False
    word = ''
    for char in input:
        # Check for comments
        if char == '/':
            if not in_comment:
                word += char
                in_comment = True
            elif word.endswith('/'):
                break

        # Check for single character tokens
        elif char in ';,:':
            if word:
                tokens[get_token_type(word)].add(word)
                word = ''
            tokens['Punctuation'].add(char)
        elif char in '(){}[]':
            if word:
                tokens[get_token_type(word)].add(word)
                word = ''
            tokens['Parenthesis'].add(char)

        elif char in '+-*/=':
            if word:
                tokens[get_token_type(word)].add(word)
                word = ''
            tokens['Arithmetic Operator'].add(char)
        elif char in '<>=':
            if word:
                tokens[get_token_type(word)].add(word)
                word = ''
            if char == '==':
                tokens['Logical Operator'].add('==')
            else:
                tokens['Logical Operator'].add(char)
        elif char in ' \t\n':
            if word:
                tokens[get_token_type(word)].add(word)
                word = ''
        else:
            word += char
    
    # Check for keywords, identifiers, and constants
    if word:
        tokens[get_token_type(word)].add(word)

for line in open("file.txt", 'r').read().split("\n"):
    tokenize(line)

print(f"Keyword ({len(tokens['Keyword'])}): {tokens['Keyword']}")
print(f"Identifier ({len(tokens['Identifier'])}): {tokens['Identifier']}")
print(f"Arithmetic Operator ({len(tokens['Arithmetic Operator'])}): {tokens['Arithmetic Operator']}")
print(f"Constant ({len(tokens['Constant'])}): {tokens['Constant']}")
print(f"Punctuation ({len(tokens['Punctuation'])}): {tokens['Punctuation']}")
print(f"Parenthesis ({len(tokens['Parenthesis'])}): {tokens['Parenthesis']}")