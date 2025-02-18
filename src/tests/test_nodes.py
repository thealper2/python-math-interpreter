import unittest
from src.math_interpreter.nodes import BinOp, Num
from src.math_interpreter.tokens import Token, TokenType

class TestNodes(unittest.TestCase):
    def test_num_node(self):
        token = Token(TokenType.NUMBER, 42)
        num_node = Num(token)
        self.assertEqual(num_node.value, 42)

    def test_binop_node(self):
        left = Num(Token(TokenType.NUMBER, 2))
        op = Token(TokenType.PLUS)
        right = Num(Token(TokenType.NUMBER, 3))
        binop_node = BinOp(left, op, right)
        self.assertEqual(binop_node.left, left)
        self.assertEqual(binop_node.token, op)
        self.assertEqual(binop_node.right, right)

if __name__ == "__main__":
    unittest.main()