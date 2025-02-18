import unittest
from src.math_interpreter.tokens import Token, TokenType

class TestTokens(unittest.TestCase):
    def test_token_creation(self):
        token = Token(TokenType.NUMBER, 42)
        self.assertEqual(token.type, TokenType.NUMBER)
        self.assertEqual(token.value, 42)

    def test_token_without_value(self):
        token = Token(TokenType.PLUS)
        self.assertEqual(token.type, TokenType.PLUS)
        self.assertIsNone(token.value)

if __name__ == "__main__":
    unittest.main()