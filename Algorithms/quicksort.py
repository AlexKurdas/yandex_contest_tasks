"""Quicksort."""


import sys


def quicksort(array):
    """Sorts using the "Quick sort" algorithm."""
    len_array = len(array)
    if len_array <= 1:
        return array

    middle_element_index = len_array // 2
    pivot = array[middle_element_index]
    left, center, right = partition(array, pivot)
    return quicksort(left) + center + quicksort(right)


def partition(array, pivot):
    """
    Splits the array into three different arrays relative to the
    reference element.
    """
    left, center, right = [], [], []
    for item in array:
        if item < pivot:
            left.append(item)
        elif item > pivot:
            right.append(item)
        else:
            center.append(item)
    return left, center, right


def main():
    """Reads input and prints sorted array."""
    example_array = [int(i) for i in sys.stdin.readline().strip().split()]
    result = quicksort(example_array)
    print(result)


if __name__ == '__main__':
    main()
