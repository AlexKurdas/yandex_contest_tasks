"""Calculates cumulative sums and calcelate positives."""

days_temp = [-1, -4, 8, -7, 3, 0, 1, -7, -7, 0, 0, -4, 1, 8, 1, -5, 4, 0, 7, 1]


class Sequance:
    """Returns cumulative sums sequance."""
    def __init__(self, sequance):
        self.cumulative_sums = [0]
        count = 0
        for i in sequance:
            if i > 0:
                count += 1
            self.cumulative_sums.append(count)

    def calculate_positive(self, left, right):
        """Calculates positives."""
        return self.cumulative_sums[right] - self.cumulative_sums[left]


def main():
    """Creates a class object and printing calculate_positive() result."""
    s = Sequance(days_temp)
    result = s.calculate_positive(10, 19)
    print(result)


if __name__ == '__main__':
    main()
