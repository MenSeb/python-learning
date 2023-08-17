"""Tutorial 27 - Map, Filter & Reduce."""


from functools import reduce


def main() -> None:
    """Print map, filter & reduce."""
    # Use map to print the square of each numbers rounde to three decimal places
    my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

    print(list(map(lambda x: round(x**2, 3), my_floats)))  # noqa: C417
    print([round(x**2, 3) for x in my_floats])

    # Use filter to print only the names that are less than or equal to seven letters
    my_names = ["olumide", "akinremi", "josiah", "temidayo", "omoseun"]

    print(list(filter(lambda x: len(x) < 7, my_names)))

    # Use reduce to print the product of these numbers
    my_numbers = [4, 6, 9, 23, 5]

    print(reduce(lambda x, y: x * y, my_numbers))


main()
