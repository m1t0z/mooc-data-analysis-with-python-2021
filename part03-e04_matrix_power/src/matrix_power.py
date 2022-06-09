#!/usr/bin/env python3
import numpy as np
import functools


def matrix_power(a, n: int):
    if n < 0:
        a = np.linalg.inv(a)
        n = -n
    a_n_times = (a for _ in range(n))
    m = a.shape[0]
    return functools.reduce(lambda x, y: x @ y, a_n_times, np.eye(m))


def main():
    a = np.arange(4).reshape((2, 2))
    print(f"a=\n{a}")
    print(f"matrix_power(a,2)\n={matrix_power(a,2)}")
    print(f"matrix_power(a,1)\n={matrix_power(a,1)}")
    print(f"matrix_power(a,0)\n={matrix_power(a,0)}")
    print(f"matrix_power(a,-1)\n={matrix_power(a,-1)}")
    print(f"matrix_power(a,-2)\n={matrix_power(a,-2)}")


if __name__ == "__main__":
    main()
