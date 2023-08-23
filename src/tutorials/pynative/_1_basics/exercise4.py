"""Exercise 4.

Remove first n characters from a string.
"""


class LimitError(Exception):
    """Error handling when limit is greater than the string length."""

    def __init__(self: "LimitError", limit: int, string: str) -> None:
        self.limit = limit
        self.string = string
        self.length = len(string)

    def __str__(self: "LimitError") -> str:
        return f"Limit {self.limit} must be less than the string length {self.length}."


def validate_limit(limit: int, string: str) -> None:
    """Raise if limit is greater than the length of the string."""
    if limit >= len(string):
        raise LimitError(limit, string)


def remove_chars_start(string: str, limit: int) -> str:
    """Remove characters starting from zero up to limit and return a new string."""
    validate_limit(limit, string)

    return string[limit:]


def remove_chars_end(string: str, limit: int) -> str:
    """Remove characters starting from zero up to limit and return a new string."""
    validate_limit(limit, string)

    return string[0:limit]


def main() -> None:
    """Print new strings with chars removed."""
    string = str(input("Enter a string: "))

    print(remove_chars_start(string, 4))
    print(remove_chars_start(string, 2))

    print(remove_chars_end(string, 4))
    print(remove_chars_end(string, 2))

    try:
        print(remove_chars_start(string, len(string)))
    except LimitError as error:
        print(f"LimitError was caught: {error}")


main()
