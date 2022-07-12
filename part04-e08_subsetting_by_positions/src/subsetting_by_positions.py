#!/usr/bin/env python3

import pandas as pd


def subsetting_by_positions():
    df = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    subset = df.iloc[:10, 2:4]
    return subset


def main():
    print(subsetting_by_positions())


if __name__ == "__main__":
    main()
