"""Tutorial 26 - Decorators."""

from typing import Callable, TypeVar

Type = TypeVar("Type")
ArgType = TypeVar("ArgType")


def type_check(correct_type: Type) -> Callable:
    """Create a type check generator."""

    def type_check_generator(callback: Callable) -> Callable:
        def type_check_callback(arg: ArgType) -> None:
            if type(arg) == correct_type:
                return callback(arg)

            print("Bad Type")
            return None

        return type_check_callback

    return type_check_generator


@type_check(int)
def times2(num: int) -> int:
    return num * 2


@type_check(str)
def first_letter(word: str) -> str:
    return word[0]


def main() -> None:
    """Print decorators."""
    print(times2(2))
    times2("Not A Number")

    print(first_letter("Hello World"))
    first_letter(["Not", "A", "String"])


main()
