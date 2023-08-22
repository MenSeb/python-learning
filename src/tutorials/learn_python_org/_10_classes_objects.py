"""Tutorial 10 - Classes & Objects."""


# define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def __init__(
        self: "Vehicle",
        name: str,
        kind: str,
        color: str,
        value: float,
    ) -> None:
        self.name = name
        self.kind = kind
        self.color = color
        self.value = value

    def description(self: "Vehicle") -> str:
        return f"{self.name} is a {self.color} {self.kind} worth ${self.value:.2f}."


def main() -> None:
    # your code goes here
    car1 = Vehicle("Fer", "convertible", "red", 60000.00)
    car2 = Vehicle("Jump", "van", "blue", 10000.00)

    # test code
    print(car1.description())
    print(car2.description())


main()
