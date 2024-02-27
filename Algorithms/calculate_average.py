"""Calculates average."""


import sys
from typing import List, Union


def calculate_average(data: List[int]) -> Union[int, float]:
    """Calculates average."""
    len_data = len(data)
    data_sum = data[0] + data[-1] * len_data / 2
    average = data_sum / len_data
    return average


def main():
    """Reads and printing result."""
    data = [int(i) for i in sys.stdin.readline().strip().split()]
    result = calculate_average(data)
    print(result)


if __name__ == '__main__':
    main()
