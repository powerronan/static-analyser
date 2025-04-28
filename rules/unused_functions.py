import ast

class unused_function_analyser(ast.NodeVisitor):
    def __init__(self):
        self.functions_defined = dict()
        self.functions_called = dict()

    def visit_FunctionDef(self, node):
        self.functions_defined[node.name] = node.lineno
        self.generic_visit(node)

    def visit_Call(self, node):
        if isinstance(node.func, ast.Name):
            self.functions_called[node.func.id] = node.func.lineno
        self.generic_visit(node)

def find_unused_functions(code_text):
    tree = ast.parse(code_text)

    analyser = unused_function_analyser()
    analyser.visit(tree)

    unused_names = analyser.functions_defined.keys() - analyser.functions_called.keys()

    unused = {name: analyser.functions_defined[name] for name in unused_names}
        

    return unused
