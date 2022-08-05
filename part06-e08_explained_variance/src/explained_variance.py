#!/usr/bin/env python3
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import numpy as np


def explained_variance():
    df = pd.read_csv("src/data.tsv", sep="\t")
    pca = PCA()
    pca.fit(df)
    ev = pca.explained_variance_
    v = df.var()

    return v, ev


def stringify(arr):
    return " ".join(map(lambda x: f"{x:.3f}", arr))


def main():
    v, ev = explained_variance()
    print("The variances are: " + stringify(v))
    print("The explained variances after PCA are: " + stringify(ev))

    ev_cumsum = np.cumsum(ev)
    plt.plot(np.arange(len(ev_cumsum)) + 1, ev_cumsum)

    plt.show()


if __name__ == "__main__":
    main()
