"""Tutorial 2 - Variables & Types."""


def variables_types() -> None:
    """Print variables and their types."""
    mystring: str = "hello"
    myfloat: float = 5.0
    myint: int = 4

    if isinstance(mystring, str) and mystring == "hello":
        print("String: %s" % mystring)

    if isinstance(myfloat, float) and myfloat == 5.0:
        print("Float: %f" % myfloat)

    if isinstance(myint, int) and myint == 4:
        print("Integer: %d" % myint)


def main() -> None:
    variables_types()


main()
