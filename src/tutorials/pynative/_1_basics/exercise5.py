"""Exercise 5.

Check if the first and last number of a list are the same.
"""


from __future__ import annotations


def check_list_numbers(list_numbers: list[int]) -> bool:
    """Check if the first and last number of the list are the same."""
    return list_numbers[0] == list_numbers[len(list_numbers) - 1]


def main() -> None:
    """Print if numbers from a list are the same."""
    numbers_x = [10, 20, 30, 40, 10]
    numbers_y = [75, 65, 35, 75, 30]

    print(f"List: {numbers_x}")
    print(f"Result is: {check_list_numbers(numbers_x)}")

    print(f"List: {numbers_y}")
    print(f"Result is: {check_list_numbers(numbers_y)}")


main()
