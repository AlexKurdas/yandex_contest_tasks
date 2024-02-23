"""Deletes dublicate elements in a sorted array and 
   replaces the dublicates with a symbol '_'.
"""
import sys


def deletes_dublicate(array_len, array):
    """Deletes dublicates in an array."""
    array_set = set(array)
    array_list = list(array_set)
    array_list.sort(key = int)
    for i in range(len(array_list), array_len):
        array_list.insert(i, '_')
    if len(array_list) != array_len:
        return False
    result = ' '.join(array_list)
    return result


def main():
    array_len = int(sys.stdin.readline().strip())
    array = sys.stdin.readline().strip().split()
    result = deletes_dublicate(array_len, array)
    print(result)

if __name__ == '__main__':
    main()
