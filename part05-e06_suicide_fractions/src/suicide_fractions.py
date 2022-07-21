#!/usr/bin/env python3

import pandas as pd


def suicide_fractions() -> pd.Series:
    df = pd.read_csv("src/who_suicide_statistics.csv")
    df["fraction"] = df["suicides_no"] / df["population"]
    return df.groupby("country")["fraction"].mean()


def main():
    print(suicide_fractions())


if __name__ == "__main__":
    main()
