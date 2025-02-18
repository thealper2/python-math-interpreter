from enum import Enum
from dataclasses import dataclass
from typing import Optional, Union

class TokenType(Enum):
    # Represents a numeric value
    NUMBER = 'NUMBER'
    # Represents the addition operator '+'
    PLUS = 'PLUS'
    # Represents the minus operator '-'
    MINUS = 'MINUS'
    # Represents the multiply operator '*'
    MULTIPLY = 'MULTIPLY'
    # Represents the divide operator '/'
    DIVIDE = 'DIVIDE'
    # Represents the end of the input
    EOF = 'EOF'

@dataclass
class Token:
    # The type of the token
    type: TokenType
    # The value of the token
    value: Optional[Union[str, float]] = None