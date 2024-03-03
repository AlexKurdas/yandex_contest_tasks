"""Counts how many measurements each next version takes
   (Fibonacci sequence).
"""


import sys


def fibonacci(version: int) -> int:
    """Recursively counts how many measurements each subsequent version
       takes(Fibonacci sequence).
    """
    if version == 0:
        return 1
    if version == 1:
        return 1
    return fibonacci(version - 1) + fibonacci(version - 2)


def main():
    """Reads input and prints result."""
    version = int(sys.stdin.readline().strip())
    result = fibonacci(version)
    print(result)


if __name__ == '__main__':
    main()
