"""Tutorial 25 - Closures."""

from typing import Callable


def multiplier_of(multiplier: int) -> Callable:
    """Return a function to multiply a number by multiplier."""

    def multiply(number: int) -> int:
        return number * multiplier

    return multiply


def main() -> None:
    """Print closures."""
    # your code goes here
    multiplywith5 = multiplier_of(5)
    print(multiplywith5(9))


main()
