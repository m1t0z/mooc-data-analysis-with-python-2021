#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def center(a: np.ndarray):
    cnt_rows, cnt_cols = a.shape[:2]
    center_x = (cnt_cols - 1) / 2
    center_y = (cnt_rows - 1) / 2
    return (center_y, center_x)


def radial_distance(a: np.ndarray):
    h, w = a.shape[:2]
    center_y, center_x = center(a)

    # Use "add zeroes" trick to activate broadcasting to the desired shape.
    X = np.arange(w) + np.zeros((h, w), dtype=int)
    Y = np.arange(h).reshape((h, 1)) + np.zeros((h, w), dtype=int)

    # Euclide distance.
    dist = np.sqrt(((X - center_x) ** 2) + ((Y - center_y) ** 2))

    return dist


def scale(a: np.ndarray, tmin: float = 0.0, tmax: float = 1.0):
    """Returns a copy of array 'a' with its values scaled to be in the range
    [tmin,tmax]."""

    a_min = np.min(a)
    a_max = np.max(a)
    a_range = a_max - a_min

    if a_range == 0:
        return np.full(a.shape, tmin)

    k = (tmax - tmin) / a_range
    scaled_a = (a - a_min) * k + tmin
    scaled_clipped_a = np.clip(scaled_a, tmin, tmax)

    return scaled_clipped_a


def radial_mask(a: np.ndarray):
    mask = radial_distance(a)
    mask_scaled = scale(mask)
    mask_scaled_inverted = 1 - mask_scaled
    return mask_scaled_inverted


def radial_fade(a: np.ndarray):
    m = radial_mask(a)[:, :, np.newaxis]
    return a * m


def main():
    image = plt.imread("src/painting.png")
    fig, ax = plt.subplots(3)
    ax[0].imshow(image)
    ax[1].imshow(radial_mask(image))
    ax[2].imshow(radial_fade(image))
    plt.show()


if __name__ == "__main__":
    main()
