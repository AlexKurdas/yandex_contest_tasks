"""Insertion sort."""


from typing import List


def insertion_sort(array: List[int]) -> None:
    """Sorts the given list of integers using insertion sort algorithm."""
    for i in range(1, len(array)):
        current = array[i]
        prev = i - 1
        while prev >= 0 and array[prev] > current:
            array[prev + 1] = array[prev]
            prev -= 1
        array[prev + 1] = current
        print(f'Шаг {i}, отсортировано элементов: {i + 1}, {array}')


def main():
    """Reads example list and performs insertion sort on it."""
    example_array = [2, 9, 11, 7, 1]
    insertion_sort(example_array)


if __name__ == '__main__':
    main()
