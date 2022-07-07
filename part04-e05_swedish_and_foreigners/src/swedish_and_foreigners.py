#!/usr/bin/env python3

import pandas as pd


def swedish_and_foreigners():
    df = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)

    # Subset of rows: only municipalities.
    df = df["Akaa":"Äänekoski"]

    # Subset of rows: proportion of Swedish speaking people and proportion of foreigners both above 5 % level.
    df = df[
        (df["Share of Swedish-speakers of the population, %"] > 5)
        & (df["Share of foreign citizens of the population, %"] > 5)
    ]

    # Take only 3 columns.
    df = df[
        [
            "Population",
            "Share of Swedish-speakers of the population, %",
            "Share of foreign citizens of the population, %",
        ]
    ]

    return df


def main():
    print(swedish_and_foreigners())


if __name__ == "__main__":
    main()
