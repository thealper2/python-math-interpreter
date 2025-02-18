from src.math_interpreter.parser import Parser
from src.math_interpreter.tokens import TokenType
from src.math_interpreter.nodes import AST, BinOp, Num

class Interpreter:
    def __init__(self, parser: Parser):
        # Parser to generate the AST
        self.parser = parser

    def visit_BinOp(self, node: BinOp) -> float:
        # Evaluate binary operations (+, -, *, /)
        if node.token.type == TokenType.PLUS:
            return self.visit(node.left) + self.visit(node.right)
        elif node.token.type == TokenType.MINUS:
            return self.visit(node.left) - self.visit(node.right)
        elif node.token.type == TokenType.MULTIPLY:
            return self.visit(node.left) * self.visit(node.right)
        elif node.token.type == TokenType.DIVIDE:
            right_val = self.visit(node.right)
            if right_val == 0:
                # Handle division by zero
                raise ValueError("Division by Zero Error")
            return self.visit(node.left) / right_val

    def visit_Num(self, node: Num) -> float:
        # Return the numeric value of a Num node
        return node.value

    def visit(self, node: AST) -> float:
        # Dynamically call the appropriate visit method based on the node type
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name)
        return method(node)

    def interpret(self) -> float:
        # Parse the input into an AST and evaluate it
        tree = self.parser.parse()
        return self.visit(tree)