from src.math_interpreter.lexer import Lexer
from src.math_interpreter.tokens import TokenType
from src.math_interpreter.nodes import AST, Num, BinOp

class Parser:
    def __init__(self, lexer: Lexer):
        # Lexer to tokenize the input
        self.lexer = lexer
        # Initialize the current token
        self.current_token = self.lexer.get_next_token()

    def error(self):
        # Raise an error for syntax
        raise Exception('Syntax error')

    def eat(self, token_type: TokenType):
        # Consume the current token if it matches the expected type, else raise an error
        if self.current_token.type == token_type:
            self.current_token = self.lexer.get_next_token()
        else:
            self.error()

    def factor(self) -> AST:
        # Parse a number (terminal node in the AST)
        token = self.current_token
        # Consume the NUMBER token
        self.eat(TokenType.NUMBER)
        # Return a Num node
        return Num(token)

    def term(self) -> AST:
        # Parse multiplication and division operations
        node = self.factor()

        while self.current_token.type in (TokenType.MULTIPLY, TokenType.DIVIDE):
            token = self.current_token
            if token.type == TokenType.MULTIPLY:
                # Consume the MULTIPLY token
                self.eat(TokenType.MULTIPLY)
            else:
                # Consume the DIVIDE token
                self.eat(TokenType.DIVIDE)
            
            # Create a BinOp node
            node = BinOp(left=node, op=token, right=self.factor())

        return node

    def expr(self) -> AST:
        # Parse additiion and subtraction operations
        node = self.term()

        while self.current_token.type in (TokenType.PLUS, TokenType.MINUS):
            token = self.current_token
            if token.type == TokenType.PLUS:
                # Consume the PLUS token
                self.eat(TokenType.PLUS)
            else:
                # Consume the MINUS token
                self.eat(TokenType.MINUS)

            # Create a BinOp node
            node = BinOp(left=node, op=token, right=self.term())

        return node

    def parse(self) -> AST:
        # Start parsing the input and return the root of the AST
        return self.expr()