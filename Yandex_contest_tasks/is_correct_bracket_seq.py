"""Checks for correct brackets sequence."""


import sys


def is_correct_bracket_seq(brackets: str) -> bool:
    """Checks for correct brackets sequence."""
    stack = []
    bracket_dict = {
        '}': '{',
        ']': '[',
        ')': '(',
    }
    for bracket in brackets:
        if bracket in bracket_dict.values():
            stack.append(bracket)
        elif bracket in bracket_dict.keys():
            if not stack or stack.pop() != bracket_dict[bracket]:
                return False
    return len(stack) == 0


def main():
    """Reads and printing is_correct_bracket_seq() result."""
    brackets = sys.stdin.readline().strip()
    result = is_correct_bracket_seq(brackets)
    print(result)


if __name__ == '__main__':
    main()
