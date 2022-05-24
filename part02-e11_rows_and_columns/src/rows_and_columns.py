#!/usr/bin/env python3

import numpy as np


def get_rows(a):
    rows = []
    for row_index in range(a.shape[0]):
        rows.append(a[row_index, :])
    return rows


def get_columns(a):
    cols = []
    for col_index in range(a.shape[1]):
        cols.append(a[:, col_index])
    return cols


def main():
    np.random.seed(0)
    a = np.random.randint(0, 10, (4, 4))
    print("a:\n", a)
    print("Rows:\n", get_rows(a))
    print("Columns:\n", get_columns(a))


if __name__ == "__main__":
    main()
