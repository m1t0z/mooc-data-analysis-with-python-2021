#!/usr/bin/env python3

import pandas as pd


def main():
    df: pd.DataFrame = pd.read_csv("src/municipal.tsv", sep="\t")
    r, c = df.shape
    print(f"Shape: {r},{c}")
    print("Columns:")
    for col in df.columns:
        print(col)


if __name__ == "__main__":
    main()
