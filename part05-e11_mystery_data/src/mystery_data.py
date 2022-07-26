#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LinearRegression


def mystery_data():
    df = pd.read_csv("src/mystery_data.tsv", sep="\t")

    y = df["Y"]
    X = df.iloc[:, :-1]

    # print(X.shape)
    # print(y.shape)

    reg = LinearRegression(fit_intercept=False).fit(X, y)

    return reg.coef_


def main():
    coefficients = mystery_data()
    for i, c in enumerate(coefficients):
        print(f"Coefficient of X{i+1} is {c}")


if __name__ == "__main__":
    main()
