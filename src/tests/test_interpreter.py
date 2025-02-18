import unittest
from src.math_interpreter.lexer import Lexer
from src.math_interpreter.parser import Parser
from src.math_interpreter.interpreter import Interpreter

class TestInterpreter(unittest.TestCase):
    def test_interpreter_number(self):
        lexer = Lexer("42")
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        self.assertEqual(result, 42)

    def test_interpreter_addition(self):
        lexer = Lexer("2 + 3")
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        self.assertEqual(result, 5)

    def test_interpreter_multiplication(self):
        lexer = Lexer("2 * 3")
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        self.assertEqual(result, 6)

    def test_interpreter_complex_expression(self):
        lexer = Lexer("2 + 3 * 4")
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        self.assertEqual(result, 14)

    def test_interpreter_division(self):
        lexer = Lexer("10 / 2")
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        result = interpreter.interpret()
        self.assertEqual(result, 5)

    def test_interpreter_division_by_zero(self):
        lexer = Lexer("10 / 0")
        parser = Parser(lexer)
        interpreter = Interpreter(parser)
        with self.assertRaises(ValueError):
            interpreter.interpret()

if __name__ == '__main__':
    unittest.main()