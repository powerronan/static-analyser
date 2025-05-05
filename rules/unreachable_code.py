import ast

class unreachable_code(ast.NodeVisitor):

    def __init__(self):
        self.unreachable_lines = set()

    def visit_FunctionDef(self, node):
        self._check_block(node.body)
        self.generic_visit(node)
    
    def visit_For(self, node):
        self._check_block(node.body)
        self._check_block(node.orelse)
        self.generic_visit(node)

    def visit_If(self, node):
        self._check_block(node.body)
        self._check_block(node.orelse)
        self.generic_visit(node)

    def visit_While(self, node):
        self._check_block(node.body)
        self._check_block(node.orelse)
        self.generic_visit(node)

    def _check_block(self, statements):
        dead = False
        
        for stmt in statements:
            if dead and hasattr(stmt, 'lineno'):
                self.unreachable_lines.add(stmt.lineno)

            if isinstance(stmt, (ast.Return, ast.Break, ast.Continue, ast.Raise)):
                dead = True
   
    
def detect_unreachable_code(code_text):
    tree = ast.parse(code_text)

    analyser = unreachable_code()
    analyser.visit(tree)

    return analyser.unreachable_lines


