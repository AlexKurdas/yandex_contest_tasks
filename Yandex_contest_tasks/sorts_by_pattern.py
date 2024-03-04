"""Sorts py pattern."""

import sys
from typing import List


def sorts_by_pattern(array_len: int, array: List[int], 
                     pattern_len: int, pattern: List[int]) -> str:
    """Sorts an array of integers according to an array pattern."""
    sorted_array = []
    for num in pattern:
        while num in array:
            sorted_array.append(str(num))
            array.remove(num)
    for num in sorted(array):
        sorted_array.append(str(num))
    result = ' '.join(sorted_array)
    return result


def main():
    """Reads input and prints result."""
    array_len = int(sys.stdin.readline().strip())
    array = [int(i) for i in sys.stdin.readline().strip().split()]
    pattern_len = int(sys.stdin.readline().strip())
    pattern = [int(i) for i in sys.stdin.readline().strip().split()]
    result = sorts_by_pattern(array_len, array, pattern_len, pattern)
    print(result)


if __name__ == '__main__':
    main()
