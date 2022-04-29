#!/usr/bin/env python3

import math


def solve_quadratic(a, b, c):
    v1 = math.sqrt(b**2 - 4 * a * c)
    v2 = 2 * a
    return ((-b + v1) / v2, (-b - v1) / v2)


def main():
    print(f"solve_quadratic(1,-3,2) = {solve_quadratic(1,-3,2)}")
    print(f"solve_quadratic(1,2,1) = {solve_quadratic(1,2,1)}")


if __name__ == "__main__":
    main()
