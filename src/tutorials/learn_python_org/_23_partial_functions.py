"""Tutorial 23 - Partial Functions."""

from functools import partial


def multiply(x: int, y: int) -> int:
    """Multiply x by y."""
    return x * y


def equation(u: int, v: int, w: int, x: int) -> int:
    """Multiply u by 4, v by 3, w by 2 and add everything to x."""
    return u * 4 + v * 3 + w * 2 + x


def main() -> None:
    """Print partial functions."""
    double = partial(multiply, 2)

    print(double(4))

    partial_equation = partial(equation, 5, 10, 5)

    print(partial_equation(0))


main()
