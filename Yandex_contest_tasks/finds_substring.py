"""Finds the longest substring that daes not contains dublicate characters."""


import sys


def finds_substring(string: str) -> int:
    """Returns length of longest substring."""
    string_len = len(string)
    char_set = set()
    result = 0
    pointer_1 = 0
    pointer_2 = 0
    while pointer_1 < string_len and pointer_2 < string_len:
        if string[pointer_2] not in char_set:
            char_set.add(string[pointer_2])
            pointer_2 += 1
            result = max(result, pointer_2 - pointer_1)
        else:
            char_set.remove(string[pointer_1])
            pointer_1 += 1
    return result


def main():
    """Reads and prints result."""
    string = sys.stdin.readline().strip()
    result = finds_substring(string)
    print(result)


if __name__ == '__main__':
    main()
