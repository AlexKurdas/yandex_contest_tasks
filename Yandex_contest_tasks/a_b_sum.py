import sys


def a_b_sum(a, b):
    """Returns the sum a + b."""
    return a + b


def main():
    """Reads input and returns result"""
    a = int(sys.stdin.readline().strip())
    b = int(sys.stdin.readline().strip())
    result = a_b_sum(a, b)
    print(result)


if __name__ == '__main__':
    main()
