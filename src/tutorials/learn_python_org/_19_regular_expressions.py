"""Tutorial 19 - Regular Expressions."""

from __future__ import annotations

import re


# Exercise: make a regular expression that will match an email
def test_email(regexp: str, emails: list[str]) -> None:
    """Test email with regexp and print if the test pass."""
    pattern = re.compile(regexp)

    for email in emails:
        if not re.match(pattern, email):
            print("You failed to match %s" % (email))
        elif not regexp:
            print("Forgot to enter a regular expression!")
        else:
            print("Pass")


def main() -> None:
    """Print regular expressions."""
    pattern = r".+@.+\..{3}"  # Your pattern here!
    emails = [
        "john@example.com",
        "python-list@python.org",
        "wha.t.`1an?ug{}ly@email.com",
    ]

    test_email(pattern, emails)


main()
