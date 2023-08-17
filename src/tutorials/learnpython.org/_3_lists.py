"""Tutorial 3 - Lists."""

from __future__ import annotations


def lists() -> None:
    """Print different lists."""
    numbers: list[int] = []
    strings: list[str] = []
    names = ["John", "Eric", "Jessica"]

    for x in [1, 2, 3]:
        numbers.append(x)  # noqa: PERF402

    strings.append("hello")
    strings.append("world")

    second_name = names[1]

    print("List of numbers in range (1, 4) %s" % list(range(1, 4)))
    print("List of numbers %s" % numbers)
    print("List of strings %s" % strings)
    print(
        "The second name on the list of names %s is %s"  # noqa: UP031
        % (names, second_name),
    )
    print("Using format specifiers instead, {f} with {names} and {second_name}")
    print(f"The second name on the list of names {names} is {second_name}")


def main() -> None:
    lists()


main()
