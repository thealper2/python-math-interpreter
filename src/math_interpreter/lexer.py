from src.math_interpreter.tokens import Token, TokenType

class Lexer:
    def __init__(self, text: str):
        # Remove spaces
        self.text = text.replace(" ", "")
        # Current position
        self.pos = 0
        # Current character
        self.current_char = self.text[0] if self.text else None

    def error(self):
        # Raise error for invalid characters
        raise Exception('Invalid character')

    def advance(self):
        # Move to the next character
        self.pos += 1
        # Update current character
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def skip_whitespace(self):
        # Skip any whitespace
        while self.current_char and self.current_char.isspace():
            self.advance()

    def number(self) -> float:
        result = ''
        while self.current_char and (self.current_char.isdigit() or self.current_char == '.'):
            # Parse a number
            result += self.current_char
            self.advance()

        # Return the parsed number as a float
        return float(result)

    def get_next_token(self) -> Token:
        while self.current_char:
            # Skip whitespace
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            # If character is a digit, parse the number
            if self.current_char.isdigit():
                return Token(TokenType.NUMBER, self.number())

            # If character is '+', return PLUS token
            if self.current_char == '+':
                self.advance()
                return Token(TokenType.PLUS)

            # If character is '-', return MINUS token
            if self.current_char == '-':
                self.advance()
                return Token(TokenType.MINUS)

            # If character is '*', return MULTIPLY token
            if self.current_char == '*':
                self.advance()
                return Token(TokenType.MULTIPLY)

            # If character is '/', return DIVIDE token
            if self.current_char == '/':
                self.advance()
                return Token(TokenType.DIVIDE)

            # Raise error for invalid characters
            self.error()

        # Return EOF token when end of input is reached
        return Token(TokenType.EOF)