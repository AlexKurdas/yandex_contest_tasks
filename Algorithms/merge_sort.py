"""Merge sort."""


import sys


def merge_sort(array):
    """Recursively splits the array into two halves."""
    len_array = len(array)
    if len_array <= 1:
        return array
    left = merge_sort(array[0 : len_array // 2])
    right = merge_sort(array[len_array // 2 : len_array])
    return merge(left, right)


def merge(left, right):
    """Sorts and merges array elements."""
    result = []
    left_idx, right_idx = 0, 0
    len_left, len_right = len(left), len(right)

    while left_idx < len_left and right_idx < len_right:
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
    return result + left[left_idx:] + right[right_idx:]


def main():
    """Reads input and prints sorted array."""
    array = [int(i) for i in sys.stdin.readline().strip().split()]
    result = merge_sort(array)
    print(result)


if __name__ == '__main__':
    main()
