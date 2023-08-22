"""Exercise 3.

Print characters from a string that are present at an even index number.
"""


from typing import Callable


def print_char_at_index(string: str, callback: Callable[[int], bool]) -> None:
    """Display characters from string if callback returns true."""
    for index, char in enumerate(string):
        if callback(index):
            print(char)


def print_char_at_index_even(string: str) -> None:
    """Display characters that are present at an even index number."""
    print("Printing only even index chars")
    print_char_at_index(string, lambda x: x % 2 < 1)


def print_char_at_index_odd(string: str) -> None:
    """Display characters that are present at an odd index number."""
    print("Printing only odd index chars")
    print_char_at_index(string, lambda x: x % 2 > 0)


def main() -> None:
    """Given a string from the user.

    Display characters that are present at an even index number.

    For example, str = "pynative", you should display `p`, `n`, `t`, `v`.
    """
    user_string = str(input("Enter a string: "))

    print(f"Original string is {user_string}")

    print_char_at_index_even(user_string)
    print_char_at_index_odd(user_string)


main()
