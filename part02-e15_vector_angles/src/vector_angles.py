#!/usr/bin/env python3

import numpy as np
import scipy.linalg


def vector_angles(X: np.ndarray, Y: np.ndarray):
    X_Y_prod = np.sum(X * Y, axis=1)
    X_norm = scipy.linalg.norm(X, 2, axis=1)
    Y_norm = scipy.linalg.norm(Y, 2, axis=1)
    X_Y_cos = X_Y_prod / (X_norm * Y_norm)
    X_Y_cos_clipped = np.clip(X_Y_cos, -1.0, 1.0)
    return np.degrees(np.arccos(X_Y_cos_clipped))


def main():
    X = np.array([[1, 2, 3], [4, 5, 6]])
    Y = np.array([[7, 8, 9], [1, 2, 3]])
    print(vector_angles(X, Y))


if __name__ == "__main__":
    main()
