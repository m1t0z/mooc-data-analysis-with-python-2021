#!/usr/bin/env python3

import numpy as np


def column_comparison(a):
    second_col = a[:, 1]
    second_last_col = a[:, -2]
    rows_mask = second_col > second_last_col
    return a[rows_mask]


def main():
    a = np.array([[0, 2, 1, 0], [0, 1, 2, 0], [0, 3, 4, 0], [0, 4, 3, 0]])
    print(a)
    print(column_comparison(a))


if __name__ == "__main__":
    main()
