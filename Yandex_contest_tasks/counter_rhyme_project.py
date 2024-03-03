"""Counter rhyme.
   N is number of participants, K is number of counting cycles
"""


import sys
from typing import List, Union


def counting_rhyme(n: int, k: int, circle: Union[List[int], None] = None,
                   current_index: int = 0) -> int:
    """Recursive counting rhyme."""
    if circle is None:
        circle = list(range(1, n + 1))
    if len(circle) == 1:
        print(circle[0])
        return
    current_index = (current_index + k - 1) % len(circle)
    circle.pop(current_index)
    counting_rhyme(n, k, circle, current_index)


def main():
    """Reads input and prints result."""
    n = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    counting_rhyme(n, k)


if __name__ == '__main__':
    main()
