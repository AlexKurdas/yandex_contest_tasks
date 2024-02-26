"""Bubble sort."""


from typing import List


def bubble_sort(data: List[int]) -> List[int]:
    """Bubble sorting."""
    last_index = len(data) - 1
    swapped = True
    while swapped:
        swapped = False
        for item_index in range(last_index):
            if data[item_index] > data[item_index + 1]:
                data[item_index], data[item_index + 1] = (
                    data[item_index + 1], data[item_index]
                )
                swapped = True
        last_index -= 1
    return data


example_array = [6, 5, 3, 1, 8, 7, 2, 4]


def main():
    """Call bubble_sort() and print result."""
    result = bubble_sort(example_array)
    print(result)


if __name__ == '__main__':
    main()
