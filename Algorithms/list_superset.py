"""Defines a superset."""


from typing import List


def list_superset(list_set_1: List[int], list_set_2: List[int]):
    """Defines a superset."""
    for item_1 in list_set_1:
        for item_2 in list_set_2:
            if item_2 in list_set_1 and len(list_set_2) < len(list_set_1):
                return f'Set {list_set_1} - superset.'
            if item_1 in list_set_2 and len(list_set_2) > len(list_set_1):
                return f'Set {list_set_2} - superset.'
            if item_1 in list_set_2 and item_2 in list_set_1:
                return 'Sets are equal.'
            return 'Superset is not found.'


list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))
