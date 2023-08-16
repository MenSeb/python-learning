"""Variables and Types."""


mystring: str = "hello"
myfloat: float = 5.0
myint: int = 4


def variables_types() -> None:
    """Print variables types."""
    if isinstance(mystring, str) and mystring == "hello":
        print("String: %s" % mystring)

    if isinstance(myfloat, float) and myfloat == 5.0:
        print("Float: %f" % myfloat)

    if isinstance(myint, int) and myint == 4:
        print("Integer: %d" % myint)


variables_types()
