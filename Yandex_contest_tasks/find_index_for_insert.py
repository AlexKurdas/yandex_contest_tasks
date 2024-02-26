"""Find index for inserting."""


import sys
from typing import List


def find_index_for_inserting(array: List[int], element: int) -> int:
    """Find index for inserting or return element index in array."""
    left = 0
    right = len(array) - 1
    if element in array:
        return array.index(element)
    while left <= right:
        mid = (left + right) // 2
        if array[mid] < element:
            left = mid + 1
        else:
            right = mid - 1
        if array[mid] < element < array[right]:
            return left
    return right + 1


def main():
    """Reads input and returns result."""
    array = [int(i) for i in sys.stdin.readline().strip().split()]
    element = int(sys.stdin.readline().strip())
    result = find_index_for_inserting(array, element)
    print(result)


if __name__ == '__main__':
    main()
