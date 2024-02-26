"""Binary search."""


wins = [1223125, 2128437, 2128500, 2741001, 4567687, 4567890, 7495938, 9314543]


def find_element(array, element):
    """Finds the element index in a sorted list."""
    left = 0
    right = len(array)

    while left < right:
        mid = (right + left) // 2
        if array[mid] == element:
            return mid
        if element > array[mid]:
            left = mid + 1
        else:
            right = mid
    return None


for item in wins:
    print(find_element(wins, item))
