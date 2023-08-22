"""Exercise 2.

Print the sum of the current number and the previous number.
"""


def main() -> None:
    """Print current and previous number sum in a range."""
    limit = 10
    n1 = 0
    for n2 in range(limit):
        print("Current Number %d Previous Number %d Sum: %d" % (n2, n1, n1 + n2))
        n1 = n2


main()
