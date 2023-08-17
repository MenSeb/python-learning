"""generators."""

import random
import secrets
from typing import Callable, Generator, Iterator


def lottery_random() -> Iterator[int]:
    """Yield random integers using random package."""
    # returns 6 numbers between 1 and 40
    for _i in range(6):
        yield random.randint(1, 40)  # noqa: S311

    # returns a 7th number between 1 and 15
    yield random.randint(1, 15)  # noqa: S311


def lottery_secrets() -> Iterator[int]:
    """Yield random integers using secrets package."""
    # returns 6 numbers between 1 and 40
    for _i in range(6):
        yield secrets.randbelow(40)

    # returns a 7th number between 1 and 15
    yield secrets.randbelow(15)


def print_lottery(lottery: Iterator[int]) -> None:
    """Print lottery numbers."""
    for number in lottery:
        print("And the next number is... %d!" % (number))


def lottery_generators() -> None:
    """Print lottery using generators."""
    print("Lottery using integers from the package random")
    print_lottery(lottery_random())
    print("\n")

    print("Lottery using integers from the package secrets")
    print_lottery(lottery_secrets())
    print("\n")


def fib() -> Iterator[int]:
    """Yield Fibonacci series using generators."""
    a, b = 0, 1

    while 1:
        yield a
        a, b = b, a + b


def print_fib(limit: int) -> None:
    """Print Fibonacci numbers."""
    counter = 0
    for n in fib():
        print(n)
        counter += 1
        if counter == limit:
            break


def test_generator(callback: Callable) -> bool:
    """Test if the callback is an instance of generator."""
    return isinstance(callback(), Generator)


def fib_generators(limit: int) -> None:
    """Print Fibonacci series using generators."""
    if test_generator(fib):
        print_fib(limit)


def main() -> None:
    """Print generators."""
    lottery_generators()

    fib_generators(20)


main()
