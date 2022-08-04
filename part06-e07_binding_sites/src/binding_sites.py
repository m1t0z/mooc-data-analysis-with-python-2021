#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn.cluster import AgglomerativeClustering
from sklearn.metrics import accuracy_score
from sklearn.metrics import pairwise_distances
from matplotlib import pyplot as plt
import seaborn as sns
import scipy

sns.set(color_codes=True)
import scipy.spatial as sp
import scipy.cluster.hierarchy as hc


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        new_label = scipy.stats.mode(real_labels[idx])[0][
            0
        ]  # Choose the most common label among data points in the cluster
        permutation.append(new_label)
    return permutation


def toint(nucleotide: str) -> int:
    d = dict(zip("ACGT", range(4)))
    return d[nucleotide]


def get_features_and_labels(filename):
    df = pd.read_csv(filename, sep="\t")
    features = (
        df["X"]
        .str.split("", expand=True)
        .iloc[:, 1:-1]
        .applymap(toint)
        .to_numpy(dtype=int)
    )
    labels = df["y"].to_numpy(dtype=int)
    return (features, labels)


def plot(distances, method="average", affinity="euclidean"):
    mylinkage = hc.linkage(sp.distance.squareform(distances), method=method)
    g = sns.clustermap(distances, row_linkage=mylinkage, col_linkage=mylinkage)
    g.fig.suptitle(
        f"Hierarchical clustering using {method} linkage and {affinity} affinity"
    )
    plt.show()


def cluster_euclidean(filename):
    features, labels_true = get_features_and_labels(filename)

    labels_predicted = (
        AgglomerativeClustering(2, affinity="euclidean", linkage="average")
        .fit(features)
        .labels_
    )

    perm = find_permutation(2, labels_true, labels_predicted)
    labels_predicted = [perm[label] for label in labels_predicted]

    return accuracy_score(labels_true, labels_predicted)


def cluster_hamming(filename):
    features, labels_true = get_features_and_labels(filename)
    features_dist = pairwise_distances(features, metric="hamming")

    labels_predicted = (
        AgglomerativeClustering(2, affinity="precomputed", linkage="average")
        .fit(features_dist)
        .labels_
    )

    perm = find_permutation(2, labels_true, labels_predicted)
    labels_predicted = [perm[label] for label in labels_predicted]

    return accuracy_score(labels_true, labels_predicted)


def main():
    print(
        "Accuracy score with Euclidean affinity is", cluster_euclidean("src/data.seq")
    )
    print("Accuracy score with Hamming affinity is", cluster_hamming("src/data.seq"))


if __name__ == "__main__":
    main()
