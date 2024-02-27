"""Calculates cumulative sums and calcelate positives."""


from typing import List

days_temp = [-1, -4, 8, -7, 3, 0, 1, -7, -7, 0, 0, -4, 1, 8, 1, -5, 4, 0, 7, 1]
cumulative_sums = [0]


def calculate_cumulative_sums(sequance: List[int]) -> List[int]:
    """Calculates cumulative sums."""
    count = 0
    for item in sequance:
        if item > 0:
            count += 1
        cumulative_sums.append(count)
    return cumulative_sums


def calculate_positives(left, right):
    """Calculates positives."""
    return cumulative_sums[right] - cumulative_sums[left]


def main():
    """Calls calculate_cumulative_sums() and
       printing calculate_positive() result.
    """
    calculate_cumulative_sums(days_temp)
    print(calculate_positives(10, 19))


if __name__ == '__main__':
    main()
