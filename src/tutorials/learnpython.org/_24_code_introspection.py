"""Tutorial 24 - Code Introspection."""


# Define the Vehicle class.
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self: "Vehicle") -> str:
        return f"{self.name} is a {self.color} {self.kind} worth ${self.value:.2f}."


def main() -> None:
    """Print code introspection."""
    help(dir)
    help(hasattr)
    help(id)

    # Print a list of all attributes of the Vehicle class.
    # Your code goes here
    print(dir(Vehicle))

    print([attr for attr in dir(Vehicle) if not attr.__contains__("__")])


main()
