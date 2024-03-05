"""Counting sort."""


def counting_sort(array, maximum):
    """Sorts an array using the "counting sort" algorithm."""
    count = [0] * (maximum + 1)
    for item in array:
        count[item] += 1

    sorted_array = []
    for item in range(maximum + 1):
        sorted_array += [item] * count[item]
    return sorted_array


array = [8, 1, 4, 10, 4, 1, 4, 7, 6, 8, 6, 4, 5, 10, 1, 0, 5, 4, 9, 7]
result = counting_sort(array, 10)
print(result)
