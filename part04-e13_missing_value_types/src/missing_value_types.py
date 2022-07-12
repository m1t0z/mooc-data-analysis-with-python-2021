#!/usr/bin/env python3

import pandas as pd
import numpy as np


def missing_value_types() -> pd.DataFrame:
    state = pd.Series(
        ["United Kingdom", "Finland", "USA", "Sweden", "Germany", "Russia"]
    )
    year = pd.Series([np.nan, 1917, 1776, 1523, np.nan, 1992])
    president = pd.Series([None, "Niinistö", "Trump", None, "Steinmeier", "Putin"])
    df = pd.DataFrame(
        {"State": state, "Year of independence": year, "President": president}
    ).set_index("State")
    return df


def main():
    print(missing_value_types())


if __name__ == "__main__":
    main()
