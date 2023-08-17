"""Tutorial 18 - Function Arguments."""


from __future__ import annotations


def foo(a: int, b: int, c: int, *rest: int) -> int:
    """Print a, b & c and return the number of extra arguments."""
    print(a, b, c)
    return len(rest)


def bar(a: int, b: int, c: int, **options: int) -> bool:
    """Print a, b & c and return true if the option magicnumber is worth 7."""
    print(a, b, c)
    return options.get("magicnumber") == 7


def main() -> None:
    """Print multiple function arguments."""
    # test code
    if foo(1, 2, 3, 4) == 1:
        print("Good.")
    if foo(1, 2, 3, 4, 5) == 2:
        print("Better.")
    if bar(1, 2, 3, magicnumber=6) is False:
        print("Great.")
    if bar(1, 2, 3, magicnumber=7) is True:
        print("Awesome!")


main()
