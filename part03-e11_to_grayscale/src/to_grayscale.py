#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt


def to_grayscale(image):
    return image[:, :, 0] * 0.2126 + image[:, :, 1] * 0.7152 + image[:, :, 2] * 0.0722


def to_red(image):
    red_image = image.copy()
    red_image[:, :, 1:3] = 0
    return red_image


def to_green(image):
    green_image = image.copy()
    green_image[:, :, 0::2] = 0
    return green_image


def to_blue(image):
    blue_image = image.copy()
    blue_image[:, :, 0:2] = 0
    return blue_image


def main():
    image = plt.imread("src/painting.png")
    plt.imshow(to_grayscale(image), cmap="gray")
    _, ax = plt.subplots(3)
    ax[0].imshow(to_red(image))
    ax[1].imshow(to_green(image))
    ax[2].imshow(to_blue(image))

    plt.show()


if __name__ == "__main__":
    main()
