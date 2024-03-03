"""Calculates the number of platform for transportation."""


import sys
from typing import List


def calculates_platforms(robots_weight: List[int], weight_limit: int) -> int:
    """Calculates platforms for delivery robot."""
    sorted_weight = sorted(robots_weight)
    left_pointer = 0
    right_pointer = len(robots_weight) - 1
    platforms = 0
    while left_pointer <= right_pointer:
        weight_sum = sorted_weight[left_pointer] + sorted_weight[right_pointer]
        platforms += 1
        right_pointer -= 1
        if weight_sum <= weight_limit:
            left_pointer += 1
    return platforms


def main():
    """Reads input and calls calculates_platforms().
       Entering robot weights integer numbers separated by spaces.
    """
    robots_weight = [int(i) for i in sys.stdin.readline().strip().split()]
    weight_limit = int(sys.stdin.readline().strip())
    result = calculates_platforms(robots_weight, weight_limit)
    print(result)


if __name__ == '__main__':
    main()
