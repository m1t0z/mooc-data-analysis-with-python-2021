#!/usr/bin/env python3

import scipy.stats
import numpy as np


def load():
    import pandas as pd

    return pd.read_csv("src/iris.csv").drop("species", axis=1).values


def lengths():
    d = load()
    sepal_length = d[:, 0]
    petal_length = d[:, 2]
    return scipy.stats.pearsonr(sepal_length, petal_length)[0]


def correlations():
    d = load()
    return np.corrcoef(d, rowvar=False)


def main():
    print(lengths())
    print(correlations())


if __name__ == "__main__":
    main()
