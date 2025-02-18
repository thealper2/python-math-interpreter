import unittest
from unittest.mock import patch
from io import StringIO
from src.math_interpreter.cli import main

class TestCLI(unittest.TestCase):
    @patch('builtins.input', side_effect=["2 + 3", "q"])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_program(self, mock_stdout, mock_input):
        main()
        output = mock_stdout.getvalue()
        self.assertIn("# : 5.0", output)

if __name__ == '__main__':
    unittest.main()