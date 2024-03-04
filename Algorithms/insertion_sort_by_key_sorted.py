"""Insertion sort by key using the built-in sorted() function."""


digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6, 6, 11, 10]


def card_strength(index: int) -> int:
    """Returns the number of letters for index."""
    return digit_lengths[index]


def main():
    """Reads example and prints result."""
    cards = [2, 9, 11, 7, 1]
    result = sorted(cards, key=card_strength)
    print(result)


if __name__ == '__main__':
    main()
