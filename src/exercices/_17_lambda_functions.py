"""Tutorial 17 - Lambda Functions."""


def main() -> None:
    """Print lambda functions."""
    is_odd = lambda x: x % 2 > 0  # noqa: E731
    numbers = [2, 4, 7, 3, 14, 19]

    for number in numbers:
        print("Is number %d odd ? %s" % (number, is_odd(number)))


main()
