#!/usr/bin/env python3

import scipy
from sklearn import datasets
from sklearn import cluster
from sklearn import metrics
import pandas as pd


def find_permutation(n_clusters, real_labels, labels):
    permutation = []
    for i in range(n_clusters):
        idx = labels == i
        # Choose the most common label among data points in the cluster
        new_label = scipy.stats.mode(real_labels[idx])[0][0]
        permutation.append(new_label)
    return permutation


def plant_clustering():
    X, y = datasets.load_iris(return_X_y=True)
    model = cluster.KMeans(3, random_state=0)
    model.fit(X)
    permutation = find_permutation(3, y, model.labels_)
    acc = metrics.accuracy_score(y, [permutation[label] for label in model.labels_])
    return acc


def main():
    print(plant_clustering())


if __name__ == "__main__":
    main()
