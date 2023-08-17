"""Tutorial 12 - Modules & Packages."""

from __future__ import annotations

import re


def main() -> None:
    # Your code goes here
    find_members: list[str] = []
    members = dir(re)

    for member in members:
        if member.__contains__("find"):
            find_members.append(member)  # noqa: PERF401

    print(sorted(find_members))

    find_members_comprehension = [f for f in dir(re) if "find" in f]

    print(sorted(find_members_comprehension))


main()
