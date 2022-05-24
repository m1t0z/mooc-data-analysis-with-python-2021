#!/usr/bin/env python3

import numpy as np


def diamond(n):
    identity_m = np.eye(n, dtype=np.integer)
    identity_flipped_m = np.fliplr(identity_m)
    # Note: or use np.hstack instead
    top_half = np.concatenate((identity_flipped_m[:, :-1], identity_m), axis=1)
    bottom_half = np.flipud(top_half)
    return np.vstack((top_half, bottom_half[1:, :]))


def main():
    print(diamond(0))
    print(diamond(1))
    print(diamond(2))
    print(diamond(3))
    print(diamond(4))


if __name__ == "__main__":
    main()
