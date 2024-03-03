"""Sliding window method.
   No input sorting required.
"""


import sys
from typing import List


def finds_min_slice_sum(data: List[int], elements_in_slice: int) -> int:
    """Finds the minimum sum of elements in a slice."""
    window_sum = sum(data[0:elements_in_slice])
    min_sum = window_sum
    for index in range(elements_in_slice, len(data)):
        window_sum += (data[index] - data[index - elements_in_slice])
        min_sum = min(min_sum, window_sum)
    return min_sum


def main():
    """Reads and prints result."""
    data = [int(i) for i in sys.stdin.readline().strip().split()]
    elements_in_slice = int(sys.stdin.readline().strip())
    result = finds_min_slice_sum(data, elements_in_slice)
    print(result)


if __name__ == '__main__':
    main()
