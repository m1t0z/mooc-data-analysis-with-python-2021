#!/usr/bin/env python3

import pandas as pd


def top_bands() -> pd.DataFrame:
    df_top = pd.read_csv("src/UK-top40-1964-1-2.tsv", sep="\t")
    df_bands = pd.read_csv("src/bands.tsv", sep="\t")

    df_top["Artist"] = df_top["Artist"].str.upper()
    df_bands["Band"] = df_bands["Band"].str.upper()

    df = pd.merge(df_top, df_bands, left_on="Artist", right_on="Band")
    return df


def main():
    print(top_bands())


if __name__ == "__main__":
    main()
