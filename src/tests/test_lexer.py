import unittest
from src.math_interpreter.lexer import Lexer
from src.math_interpreter.tokens import TokenType

class TestLexer(unittest.TestCase):
    def test_number_token(self):
        lexer = Lexer("42")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.NUMBER)
        self.assertEqual(token.value, 42)

    def test_plus_token(self):
        lexer = Lexer("+")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.PLUS)

    def test_minus_token(self):
        lexer = Lexer("-")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.MINUS)

    def test_multiply_token(self):
        lexer = Lexer("*")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.MULTIPLY)

    def test_divide_token(self):
        lexer = Lexer("/")
        token = lexer.get_next_token()
        self.assertEqual(token.type, TokenType.DIVIDE)

    def test_expression_tokens(self):
        lexer = Lexer("2 + 3 * 4")
        tokens = []
        while True:
            token = lexer.get_next_token()
            tokens.append(token)
            if token.type == TokenType.EOF:
                break

        expected_types = [
            TokenType.NUMBER,
            TokenType.PLUS,
            TokenType.NUMBER,
            TokenType.MULTIPLY,
            TokenType.NUMBER,
            TokenType.EOF
        ]

        self.assertEqual([t.type for t in tokens], expected_types)

if __name__ == "__main__":
    unittest.main()