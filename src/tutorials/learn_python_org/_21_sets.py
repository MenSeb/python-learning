"""Tutorial 21 - Sets."""


def main() -> None:
    """Print sets."""
    a = ["Jake", "John", "Eric"]
    b = ["John", "Jill"]

    set_a = set(a)
    set_b = set(b)

    print("Set A %s" % set_a)
    print("Set B %s" % set_b)
    print("Participants from A not in B %s" % set_a.difference(set_b))


main()
