#!/usr/bin/env python3

import numpy as np
import pandas as pd


def last_week() -> pd.DataFrame:
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")

    # Cast all position-like columns to numeric-types (use NaNs for missing values).
    df["Pos"] = pd.to_numeric(df["Pos"], errors="coerce")
    df["LW"] = pd.to_numeric(df["LW"], errors="coerce")
    df["Peak Pos"] = pd.to_numeric(df["Peak Pos"], errors="coerce")

    # Update "peak position" column.
    m = (df["Pos"] == df["Peak Pos"]) & (df["Pos"] < df["LW"])
    df.loc[m, "Peak Pos"] = pd.NA

    # Use "last week position" as initial "current position".
    df["Pos"] = df["LW"]

    # Remove all rows with unknown "current position".
    df = df.dropna(subset=["Pos"])

    # Sort by "current position" column
    df.sort_values(by=["Pos"], inplace=True)

    # Reindex in range [1,40]: fill with nans for missing rows.
    # Details: https://stackoverflow.com/a/25916109/13396363
    df = df.set_index("Pos").reindex(np.arange(1, 41)).reset_index()

    # Update "last week" column.
    df["LW"] = pd.NA

    # Update "Weeks on Chart" column.
    df["WoC"] = df["WoC"] - 1

    return df


def main():
    df = last_week()
    print("Shape: {}, {}".format(*df.shape))
    print("dtypes:\n", df.dtypes)
    print(df)


if __name__ == "__main__":
    main()
