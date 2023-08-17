"""Tutorial 3 - Lists."""

from __future__ import annotations


def lists() -> None:
    """Print lists."""
    numbers: list[int] = []
    strings: list[str] = []
    names = ["John", "Eric", "Jessica"]

    for x in [1, 2, 3]:
        numbers.append(x)  # noqa: PERF402

    strings.append("hello")
    strings.append("world")

    second_name = names[1]

    print(list(range(1, 4)))
    print(numbers)
    print(strings)
    print("The second name on the names list is %s" % second_name)


lists()
