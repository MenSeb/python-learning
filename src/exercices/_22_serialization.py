"""serialization."""

from __future__ import annotations

import json
import pickle


# fix this function, so it adds the given name
# and salary pair to salaries_json, and return it
def add_employee(salaries_json: str, name: str, salary: int) -> str:
    """Load json and add key:val to it."""
    salaries_dict: dict[str, int] = json.loads(salaries_json)
    salaries_dict[name] = salary
    return json.dumps(salaries_dict)


def main() -> None:
    """Print serialization."""
    numbers = [1, 2, 3, "a", "b", "c"]

    json_string = json.dumps(numbers)
    print("Form json %s" % json_string)

    pickle_bytes = pickle.dumps(numbers)
    pickle_string = pickle.loads(pickle_bytes)  # noqa: S301
    print("Form pickle bytes %r" % pickle_bytes)
    print("Form pickle string %s" % pickle_string)

    # test code
    salaries = '{"Alfred" : 300, "Jane" : 400 }'
    new_salaries = add_employee(salaries, "Me", 800)
    decoded_salaries = json.loads(new_salaries)
    print(decoded_salaries["Alfred"])
    print(decoded_salaries["Jane"])
    print(decoded_salaries["Me"])


main()
