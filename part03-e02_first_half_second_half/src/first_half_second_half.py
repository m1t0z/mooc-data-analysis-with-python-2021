#!/usr/bin/env python3

import numpy as np


def first_half_second_half(a):
    m = a.shape[1] // 2
    left_half = a[:, :m]
    right_half = a[:, m:]
    left_half_column_sum = np.sum(left_half, axis=1)
    right_half_column_sum = np.sum(right_half, axis=1)
    mask = left_half_column_sum > right_half_column_sum
    return a[mask]


def main():
    a = np.array([[1, 3, 4, 2], [2, 2, 1, 2], [4, 4, 2, 2]])
    print(a)
    print(first_half_second_half(a))


if __name__ == "__main__":
    main()
