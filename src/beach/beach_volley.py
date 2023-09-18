"""Beach Volley Stats 2023."""

from __future__ import annotations

import os
from pathlib import Path

import openpyxl
import pandas as pd
from openpyxl.styles import Alignment


def read_lines(path: str) -> list[str]:
    """Read and Extract lines from beach stats file."""
    with Path.open(path, encoding="utf-8") as file:
        lines = file.readlines()

    file.close()

    return lines


def filter_lines(lines: list[str]) -> list[str]:
    """Filter empty lines."""
    return filter(lambda line: line != "\n", lines)


def format_lines(lines: list[str]) -> list[str]:
    """Remove new line and split { - } character."""
    return (line.replace("\n", "").split(" - ") for line in lines)


def format_to_csv(keys: list[str], lines: list[str]) -> list[dict[str, str]]:
    """Create a dictionnay from keys and values in lines."""
    csv_list = []

    for values in lines:
        csv_dict = {}

        for idx, key in enumerate(keys):
            try:
                value = values[idx]
            except IndexError:
                value = 0
            csv_dict[key] = value

        csv_list.append(csv_dict)

    return csv_list


def style_file_excel(path: str) -> None:
    """Style a Excel file."""
    workbook = openpyxl.open(path)
    worksheet = workbook.get_sheet_by_name("Beach 2023")

    worksheet.sheet_format.defaultRowHeight = 50
    worksheet.sheet_format.defaultColWidth = 10

    for row in worksheet[1 : worksheet.max_row]:
        row[3].alignment = Alignment(
            horizontal="center",
            vertical="center",
            wrap_text=True,
        )

    dimensions = {
        "A": {
            "width": 25,
        },
        "B": {
            "width": 20,
        },
        "D": {
            "width": 30,
        },
        "E": {
            "width": 20,
        },
    }

    for dimensions_key, dimensions_value in dimensions.items():
        column = worksheet.column_dimensions[dimensions_key]
        column.width = dimensions_value["width"]

    workbook.save(path)


def create_file_excel(data: list[str], path: str, fields: list[str]) -> None:
    """Create Excel file from lines."""
    pd.DataFrame(data, columns=fields).style.set_properties(
        **{
            "font-size": "16px",
            "text-align": "center",
            "vertical-align": "middle",
        },
    ).to_excel(
        path,
        index=False,
        header=True,
        sheet_name="Beach 2023",
    )


def main(path_txt: str, path_xls: str) -> None:
    """Extract, Format & Write to CSV the beach stats file.

    File Format:

    {DATE}-{WHERE}-{LEVEL}-{WHO}-{RESULT}-{SETS (21)}-{SETS (15)}-{SETS (25)}

    With spaces around the character "-".
    """
    fields = [
        "DATE",
        "WHERE",
        "LEVEL",
        "WHO",
        "RESULT",
        "SETS (21)",
        "SETS (15)",
        "SETS (25)",
    ]

    content = format_lines(filter_lines(read_lines(path_txt)))

    os.system("TASKKILL /F /IM excel.exe")

    create_file_excel(format_to_csv(fields, content), path_xls, fields)

    style_file_excel(path_xls)

    os.startfile(path_xls)
