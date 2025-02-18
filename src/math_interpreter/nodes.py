from src.math_interpreter.tokens import Token

class AST:
    # Base class for all Abstract Syntax Tree (AST) nodes
    pass

class BinOp(AST):
    def __init__(self, left: AST, op: Token, right: AST):
        # Left child node (AST)
        self.left = left
        # Operator token
        self.token = op
        # Right child node (AST)
        self.right = right

class Num(AST):
    def __init__(self, token: Token):
        # Token representing the number
        self.token = token
        # Numeric value of the token
        self.value = token.value