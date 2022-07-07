#!/usr/bin/env python3

import pandas as pd


def growing_municipalities(df: pd.DataFrame):

    # Subset: municipalities with increasing population.
    df_inc_population = df[df["Population change from the previous year, %"] > 0]

    ratio = df_inc_population.shape[0] / df.shape[0]
    return ratio


def main():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    df = df["Akaa":"Äänekoski"]
    percent = growing_municipalities(df) * 100
    print(f"Proportion of growing municipalities: {percent:.1f}%")


if __name__ == "__main__":
    main()
