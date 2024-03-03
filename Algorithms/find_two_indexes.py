"""Two pointer method for sorted data."""

from typing import List


def find_two_indexes(data: List[int], expected_result: int) -> tuple:
    """Returns the indices of two numbers,
       whose sum is equal to a given number.
    """
    left_pointer = 0
    right_pointer = len(data) - 1
    while left_pointer < right_pointer:
        numbers_sum = data[left_pointer] + data[right_pointer]
        if numbers_sum == expected_result:
            return left_pointer, right_pointer
        elif numbers_sum > expected_result:
            right_pointer -= 1
        else:
            left_pointer += 1


def main():
    """Reads example data and returs result."""
    data = [1, 2, 3, 4, 5, 6, 7, 11]
    expected_result = 10
    result = find_two_indexes(data, expected_result)
    print(result)


if __name__ == '__main__':
    main()
