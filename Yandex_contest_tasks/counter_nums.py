"""Counts the number of numbers in the array less than the specified number."""


import sys
from typing import List


def counts_number(numbers: List[int]) -> str:
    """Counts how many numbers in the array are less than the current one."""
    result = []
    numbers_2 = numbers
    for number in numbers:
        count = 0
        for number_2 in numbers_2:
            if number > number_2:
                count += 1
        result.append(str(count))
    return ' '.join(result)


def main():
    """Reads and prints counts_number() result."""
    numbers = [int(i) for i in sys.stdin.readline().strip().split()]
    result = counts_number(numbers)
    print(result)


if __name__ == '__main__':
    main()
