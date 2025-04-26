import ast

def find_unused_variables(code_text):
    tree = ast.parse(code_text)

    