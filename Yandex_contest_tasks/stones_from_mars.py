"""Greedy algorithms."""


import sys


def stones_from_mars(n, n_num, m, m_num):
    """Distributes in an optimal way."""
    sorted_n_num = sorted(n_num)
    sorted_m_num = sorted(m_num)
    count = 0
    n_idx = 0
    m_idx = 0
    while n_idx < n and m_idx < m:
        if sorted_m_num[m_idx] >= sorted_n_num[n_idx]:
            count += 1
            n_idx += 1
        m_idx += 1
    return count


def main():
    """Reads input and prints result."""
    n = int(sys.stdin.readline().strip())
    n_num = [int(i) for i in sys.stdin.readline().strip().split()]
    m = int(sys.stdin.readline().strip())
    m_num = [int(i) for i in sys.stdin.readline().strip().split()]
    result = stones_from_mars(n, n_num, m, m_num)
    print(result)


if __name__ == '__main__':
    main()
