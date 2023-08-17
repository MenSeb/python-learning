"""Tutorial 13 - Numpy Arrays."""

import numpy as np


def main() -> None:
    """Print weight in lbs using numpy."""
    weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

    # Create np_weight_lbs from np_weight_kg
    np_weight_kg = np.array(weight_kg)
    np_weight_lbs = np_weight_kg * 2.2

    # Print out np_weight_lbs
    print(np_weight_lbs)


main()
