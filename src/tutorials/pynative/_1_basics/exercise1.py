"""Exercise 1: Calculate the multiplication and sum of two numbers."""


def multiplication(x: int, y: int) -> int:
    """Return the product of x and y."""
    return x * y


def summation(x: int, y: int) -> int:
    """Return the sum of x and y."""
    return x + y


def product_or_sum(x: int, y: int) -> int:
    """Given two integer numbers.

    if the product is <= 1000, return their product

    else return their sum.
    """
    result = multiplication(x, y)

    if result > 1000:
        result = summation(x, y)

    return result


def main() -> None:
    """Print result."""
    n1 = 20
    n2 = 30
    print("number1 = %d" % n1)
    print("number2 = %d" % n2)
    print("The result is %d" % product_or_sum(n1, n2))

    n1 = 40
    n2 = 30
    print("number1 = %d" % n1)
    print("number2 = %d" % n2)
    print("The result is %d" % product_or_sum(n1, n2))


main()
