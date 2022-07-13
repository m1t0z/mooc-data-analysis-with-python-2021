#!/usr/bin/env python3

import pandas as pd
import numpy as np


def special_missing_values() -> pd.DataFrame:
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    # Cast "LW" column from str to float ("Re", "New" values are replaced with NaN).
    df["LW"] = pd.to_numeric(df["LW"], errors="coerce")

    # Keep only the records that drop their position.
    m = df["Pos"] > df["LW"]
    df = df[m]

    # Cast "LW" columnt from float to int.
    df["LW"] = pd.to_numeric(df["LW"], downcast="integer")

    return df


def main():
    print(special_missing_values())


if __name__ == "__main__":
    main()
