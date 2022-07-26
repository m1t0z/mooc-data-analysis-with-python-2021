#!/usr/bin/env python3

import pandas as pd
import numpy as np
from sklearn import linear_model


def coefficient_of_determination():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")

    coeffs = []

    # All features together.
    X = df.iloc[:, :-1]
    y = df.iloc[:, -1]
    reg = linear_model.LinearRegression().fit(X, y)
    coeffs.append(reg.score(X, y))

    # All features independently.
    cnt_features = len(df.columns) - 1
    for i in range(cnt_features):
        X = df.iloc[:, i].to_numpy()[:, np.newaxis]
        # print(X.shape)
        reg = linear_model.LinearRegression().fit(X, y)
        coeffs.append(reg.score(X, y))

    return coeffs


def main():
    coeffs = coefficient_of_determination()

    print(f"R2=score with features(s) X: {coeffs[0]}")
    for i, c in enumerate(coeffs[1:]):
        print(f"R2=score with features(s) X{i+1}: {c}")


if __name__ == "__main__":
    main()
