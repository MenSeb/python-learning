"""Tutorial 5 - String Formatting."""


def string_formatting() -> None:
    """Print string formatting."""
    data = ("John", "Doe", 53.44)
    format_string = "Hello %s %s. Your current balance is $%.2f"

    print(format_string % data)


string_formatting()
