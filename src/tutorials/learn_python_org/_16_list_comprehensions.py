"""Tutorial 16 - List Comprehensions."""

from __future__ import annotations

from typing import Callable, Sequence


def filter_positive(
    numbers: Sequence[int | float],
    callback: Callable | None = None,
) -> list[int | float]:
    """Filter a list of numbers keeping only the positives."""
    return [callback(n) if callback else n for n in numbers if n >= 0]


def main() -> None:
    """Print list comprehensions."""
    numbers_float = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]
    positive_numbers_float = filter_positive(numbers_float)

    print("Positive numbers float")
    print(positive_numbers_float, "\n")

    numbers_int = [34, -203, 44, 68, -12, 44, 12]
    positive_numbers_int = filter_positive(numbers_int)

    print("Positive numbers int")
    print(positive_numbers_int, "\n")

    numbers_mix = [34.6, -203.4, 44.9, 68, -12, 44, 12.7]
    positive_numbers_mix = filter_positive(numbers_mix)

    print("Positive numbers mix")
    print(positive_numbers_mix, "\n")

    positive_numbers_converted = filter_positive(numbers_float, int)

    print("Positive numbers converted to integers")
    print(positive_numbers_converted, "\n")


main()
