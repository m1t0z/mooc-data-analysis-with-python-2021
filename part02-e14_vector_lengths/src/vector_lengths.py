#!/usr/bin/env python3

import numpy as np


def vector_lengths(a: np.ndarray):
    return np.sqrt(np.sum(a * a, axis=1))


def main():
    rng = np.random.default_rng(42)
    a = rng.integers(100, size=(3, 3))
    print(f"Input:\n{a}")
    print(f"Output:\n{vector_lengths(a)}")


if __name__ == "__main__":
    main()
