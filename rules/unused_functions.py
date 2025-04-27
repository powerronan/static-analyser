import ast

class unused_function_analyser(ast.NodeVisitor):
    def __init__(self):
        self.functions_defined = set()
        self.functions_called = set()

    def visit_FunctionDef(self, node):
        self.functions_defined.add(node.name)
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.functions_called.add(node.func.id)
        self.generic_visit(node)

def find_unused_functions(code_text):
    tree = ast.parse(code_text)

    analyser = unused_function_analyser()
    analyser.visit(tree)

    unused = analyser.functions_defined - analyser.functions_called

    return unused
