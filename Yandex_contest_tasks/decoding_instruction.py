"""The module decrypts the received compressed command."""


import sys
from typing import Final

MULTIPLIER_CONSTANT: Final[int] = 10


def decode_instruction(string: str) -> str:
    """Decrypts compressed command."""
    stack = []
    current_number = 0
    current_string = ''
    for char in string:
        if char.isdigit():
            current_number = current_number * MULTIPLIER_CONSTANT + int(char)
        elif char == '[':
            stack.append((current_number, current_string))
            current_number = 0
            current_string = ''
        elif char == ']':
            number, prev_string = stack.pop()
            current_string = prev_string + number * current_string
        else:
            current_string += char
    return current_string


def main():
    """Reads input and prints result."""
    string = sys.stdin.readline().strip()
    result = decode_instruction(string)
    print(result)


if __name__ == '__main__':
    main()
