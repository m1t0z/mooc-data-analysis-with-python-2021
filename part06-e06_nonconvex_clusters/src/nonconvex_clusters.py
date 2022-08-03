#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import scipy

_plot = False


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def nonconvex_clusters():
    df = pd.read_csv("src/data.tsv", sep="\t")

    X = df.loc[:, "X1":"X2"]
    y = df["y"]
    labels_cnt = len(np.unique(y))

    epses = np.arange(0.05, 0.2, 0.05)

    _, ax = plt.subplots(len(epses))

    res = pd.DataFrame(dtype=float)

    for i, eps in enumerate(epses):
        model: DBSCAN = DBSCAN(eps).fit(X)
        outliers_cnt = sum(model.labels_ == -1)
        clusters_cnt = sum(np.unique(model.labels_) != -1)

        if clusters_cnt == labels_cnt:
            idx_no_outliers = model.labels_ != -1
            true_labels = y[idx_no_outliers]
            predicted_labels = model.labels_[idx_no_outliers]
            perm = find_permutation(clusters_cnt, true_labels, predicted_labels)
            acc = accuracy_score(
                true_labels, [perm[label] for label in predicted_labels]
            )
        else:
            acc = np.nan

        a = pd.DataFrame(
            {
                "eps": [eps],
                "Score": [acc],
                "Clusters": [clusters_cnt],
                "Outliers": [outliers_cnt],
            },
            dtype=float,
        )
        res = pd.concat([res, a], ignore_index=True)

        if _plot:
            ax[i].scatter(X.iloc[:, 0], X.iloc[:, 1], c=model.labels_)
            ax[i].set_title(f"{eps:0.2f}", loc="right")

    if _plot:
        plt.show()

    return res


def main():
    print(nonconvex_clusters())


if __name__ == "__main__":
    main()
