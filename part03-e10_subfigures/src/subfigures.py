#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def subfigures(a: np.ndarray):
    fig, ax = plt.subplots(1, 2)
    left_axes: plt.Axes = ax[0]
    right_axes: plt.Axes = ax[1]
    left_axes.plot(a[:, 0], a[:, 1])
    right_axes.scatter(a[:, 0], a[:, 1], c=a[:, 2], s=a[:, 3])
    plt.show()


def main():
    a = np.arange(25).reshape((5, 5))
    subfigures(a)


if __name__ == "__main__":
    main()
