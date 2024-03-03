"""Searches for the index of a given element in a sorted array
   using binary search via recursion.
"""

from typing import List, Union


def binary_search(
    array: List[int], element: int, left: int, right: int
) -> Union[int, None]:
    """Binary search via recursion."""
    if right < left:
        return None
    mid = (left + right) // 2
    if array[mid] == element:
        return mid
    if element < array[mid]:
        return binary_search(array, element, left, mid - 1)
    return binary_search(array, element, mid + 1, right)


def main():
    """Reads data and prints result."""
    example_array = [
        1223125,
        2128437,
        2128500,
        2741001,
        4567687,
        4567890,
        7495938,
        9314543,
    ]
    example_element = 9314543
    left = 0
    right = len(example_array) - 1
    result = binary_search(example_array, example_element, left, right)
    print(result)


if __name__ == "__main__":
    main()
