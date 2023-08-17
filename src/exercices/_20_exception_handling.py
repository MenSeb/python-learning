"""exception handling."""


from __future__ import annotations


def get_last_name(actor: dict[str, str]) -> str:
    """Return actor last name."""
    try:
        return actor["last_name"]
    except KeyError:
        return actor["name"].split(" ")[1]


def main() -> None:
    """Print exception handling."""
    # Setup
    actor = {"name": "John Cleese", "rank": "awesome"}

    # Test code
    get_last_name(actor)
    print("All exceptions caught! Good job!")
    print("The actor's last name is %s" % get_last_name(actor))


main()
