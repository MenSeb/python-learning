"""Basic Operators."""

from __future__ import annotations

x = object()
y = object()


def create_list(obj: object) -> list[object]:
    """Create a list with 10 instances of obj."""
    return [obj] * 10


def basic_operators() -> None:
    """Print basic operators."""
    x_list = create_list(x)
    y_list = create_list(y)
    big_list = x_list + y_list

    print("x_list contains %d objects" % len(x_list))
    print("y_list contains %d objects" % len(y_list))
    print("big_list contains %d objects" % len(big_list))

    if x_list.count(x) == 10 and y_list.count(y) == 10:
        print("Almost there...")
    if big_list.count(x) == 10 and big_list.count(y) == 10:
        print("Great!")


basic_operators()
