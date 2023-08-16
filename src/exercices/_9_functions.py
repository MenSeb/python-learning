"""functions."""

from __future__ import annotations


# Modify this function to return a list of strings as defined above
def list_benefits() -> list[str]:
    return [
        "More organized code",
        "More readable code",
        "Easier code reuse",
        "Allowing programmers to share and connect code together",
    ]


# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit: str) -> str:
    # could use %s too which is not only used inside print
    return benefit + " is a benefit of functions!"


def name_the_benefits_of_functions() -> None:
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))


def main() -> None:
    name_the_benefits_of_functions()


main()
