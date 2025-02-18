import unittest
from src.math_interpreter.lexer import Lexer
from src.math_interpreter.parser import Parser
from src.math_interpreter.nodes import BinOp, Num
from src.math_interpreter.tokens import TokenType

class TestParser(unittest.TestCase):
    def test_parse_number(self):
        lexer = Lexer("42")
        parser = Parser(lexer)
        ast = parser.parse()
        self.assertIsInstance(ast, Num)
        self.assertEqual(ast.value, 42)

    def test_parse_addition(self):
        lexer = Lexer("2 + 3")
        parser = Parser(lexer)
        ast = parser.parse()
        self.assertIsInstance(ast, BinOp)
        self.assertEqual(ast.token.type, TokenType.PLUS)
        self.assertIsInstance(ast.left, Num)
        self.assertIsInstance(ast.right, Num)

    def test_parse_multiplication(self):
        lexer = Lexer("2 * 3")
        parser = Parser(lexer)
        ast = parser.parse()
        self.assertIsInstance(ast, BinOp)
        self.assertEqual(ast.token.type, TokenType.MULTIPLY)
        self.assertIsInstance(ast.left, Num)
        self.assertIsInstance(ast.right, Num)

    def test_parse_complex_expression(self):
        lexer = Lexer("2 + 3 * 4")
        parser = Parser(lexer)
        ast = parser.parse()
        self.assertIsInstance(ast, BinOp)
        self.assertEqual(ast.token.type, TokenType.PLUS)
        self.assertIsInstance(ast.right, BinOp)
        self.assertEqual(ast.right.token.type, TokenType.MULTIPLY)

if __name__ == '__main__':
    unittest.main()