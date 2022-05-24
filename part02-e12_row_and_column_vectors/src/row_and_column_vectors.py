#!/usr/bin/env python3

import numpy as np


def get_row_vectors(a):
    rows = []
    for row in a:
        rows.append(row[np.newaxis, :])
    return rows


def get_column_vectors(a):
    cols = []
    for col in a.T:
        cols.append(col[:, np.newaxis])
    return cols


def main():
    np.random.seed(0)
    a = np.random.randint(0, 10, (4, 4))
    print("a:\n", a)
    print("Row vectors:\n", get_row_vectors(a))
    print("Column vectors:\n", get_column_vectors(a))


if __name__ == "__main__":
    main()
