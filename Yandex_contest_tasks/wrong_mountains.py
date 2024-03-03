"""Findig the right mountains. A correct mountains is considered to be
   one whose heights constantly increases on the way from the foot to the top,
   and constantly desreases from the top to the foot.
"""


import sys


def wrong_mountains(array):
    """Finding the right mountains."""
    array_len = len(array)
    if array_len < 3:
        return False
    index = 0
    while index < array_len - 1 and array[index] < array[index + 1]:
        index += 1
    if index in (0, array_len - 1):
        return False
    while index < array_len - 1 and array[index] > array[index + 1]:
        index += 1
    return index == array_len - 1


def main():
    """Reads and printing wrong_mountains() result."""
    array = [int(i) for i in sys.stdin.readline().strip().split()]
    result = wrong_mountains(array)
    print(result)


if __name__ == '__main__':
    main()
