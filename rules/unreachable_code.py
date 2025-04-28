import ast

class unreachable_code(ast.NodeVisitor):

    def __init__(self):
        self.dead_stack = []
        

    def visit_FunctionDef(self, node):
        self.dead_stack.append(False)
        self.generic_visit(node)
        self.dead_stack.pop()
        
    def visit_Return(self, node):
        self.dead_stack.append(True)
        self.