"""Tutorial 14 - Pandas Basics."""

import pandas as pd


def main() -> None:
    """Write and read data from CSV and print result."""
    countries = {
        "country": ["Brazil", "Russia", "India", "China", "South Africa"],
        "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
        "area": [8.516, 17.10, 3.286, 9.597, 1.221],
        "population": [200.4, 143.5, 1252, 1357, 52.98],
    }

    path_countries: str = "datas/countries.csv"

    df_countries = pd.DataFrame(countries, ["BR", "RU", "IN", "CH", "SA"])

    # Print DataFrame
    print("DataFrame Countries")
    print(df_countries, "\n")

    # Write DataFrame to CSV file
    pd.DataFrame.to_csv(df_countries, path_countries)

    # Read data from CSV file
    csv_countries = pd.read_csv(path_countries, index_col=0)

    # Print CSV file
    print("CSV Countries")
    print(csv_countries, "\n")

    # Print capitals Series
    print("Series capitals")
    print(csv_countries["capital"], "\n")

    # Print capitals DataFrame
    print("DataFrame capitals")
    print(csv_countries[["capital"]], "\n")

    # Print capitals & population DataFrame
    print("DataFrame capitals & population")
    print(csv_countries[["capital", "population"]], "\n")

    # Print data range
    print("Data range [2:4]")
    print(csv_countries[2:4], "\n")

    # Print data for Russia
    print("Data Russia")
    print(csv_countries.iloc[1], "\n")

    # Print data for China & India
    print("Data China & India")
    print(csv_countries.loc[["CH", "IN"]], "\n")


main()
