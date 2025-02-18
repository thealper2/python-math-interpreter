from src.math_interpreter.lexer import Lexer
from src.math_interpreter.parser import Parser
from src.math_interpreter.interpreter import Interpreter

def main():
    while True:
        try:
            # Prompt user for input
            text = input('calc > ')
            
            # Exit if user types 'q'
            if text.lower() == 'q':
                break
                
            # Create a Lexer to tokenize the input
            lexer = Lexer(text)
            # Create a Parser to generate an AST from tokens
            parser = Parser(lexer)
            # Create an Interpreter to evaluate the AST
            interpreter = Interpreter(parser)
            # Interpret the input and compute the result
            result = interpreter.interpret()
            # Print the result
            print(f"# : {result}")
            
        except Exception as e:
            # Handle and display any errors
            print(f"Error: {str(e)}")