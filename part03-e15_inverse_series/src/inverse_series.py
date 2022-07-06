#!/usr/bin/env python3

import pandas as pd


def inverse_series(s: pd.Series):
    return pd.Series(s.index, s.values)


def main():
    s = pd.Series([0, 1], list("ab"), name="s")
    s_inversed = inverse_series(s)
    s_inversed.name = "s_inversed"

    print(s, s_inversed, sep="\n")


if __name__ == "__main__":
    main()
