import ast

class unused_variable_analyser(ast.NodeVisitor):
    def __init__(self):
        self.assigned = dict()
        self.used = dict()
    
    def visit_Assign(self, node):
        for target in node.targets:
            if isinstance(target, ast.Name):
                self.assigned[target.id] = target.lineno
        self.generic_visit(node)

    def visit_AugAssign(self, node):
        if isinstance(node.target, ast.Name):
            self.assigned[node.target.id] = node.target.lineno
        self.generic_visit(node)
    
    def visit_Name(self, node):
        if isinstance(node.ctx, ast.Load):
            self.used[node.id] = node.lineno
        self.generic_visit(node)

        


def find_unused_variables(code_text):
    tree = ast.parse(code_text)

    analyser = unused_variable_analyser()
    analyser.visit(tree)
    unused = analyser.assigned.keys() - analyser.used.keys()

    unused_variables = {name: analyser.assigned[name] for name in unused}

    return unused_variables


    