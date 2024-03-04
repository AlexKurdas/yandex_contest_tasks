"""Insertion sort by key using cards as an example."""


from typing import List, Union

digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6, 6, 11, 10]

card_colors = [
    'Аметистовый',   # [0]
    'Чёрный',        # [1]
    'Белый',         # [2]
    'Жёлтый',        # [3] 
    'Синий',         # [4]
    'Фиолетовый',    # [5]
    'Коричневый',    # [6]
    'Зелёный',       # [7]
    'Розовый',       # [8]
    'Серо-голубой',  # [9]
    'Бобровый',      # [10]
    'Коралловый',    # [11]
    'Ванильный'      # [12]
]


def card_strength(index: int) -> int:
    """Returns the number of letters for index."""
    return digit_lengths[index]


def card_background(index: int) -> str:
    """Returns the color for index."""
    return card_colors[index]


def insertion_sort_by_key(array: List[int],
                          key: Union[List[int], List[str]]) -> None:
    """Insertion sort by key."""
    for i in range(1, len(array)):
        current = array[i]
        prev = i - 1
        while prev >= 0 and key(array[prev]) > key(current):
            array[prev + 1] = array[prev]
            prev -= 1
        array[prev + 1] = current


def main():
    """Reads example cards and sorts by word length and color."""
    cards = [2, 9, 11, 7, 1]
    insertion_sort_by_key(cards, card_strength)
    print('Sort by word length:', cards)
    insertion_sort_by_key(cards, card_background)
    print('Sort by color:', cards)


if __name__ == '__main__':
    main()
