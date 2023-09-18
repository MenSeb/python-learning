"""Module Beach entry point."""

from pathlib import Path

from beach_volley import main

if __name__ == "__main__":
    file = "beach-2023"
    folder = f"{Path.cwd()}/src/beach/assets"

    path_txt = f"{folder}/{file}.txt"
    path_xls = f"{folder}/{file}.xlsx"

    main(path_txt, path_xls)
