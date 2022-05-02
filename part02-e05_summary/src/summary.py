#!/usr/bin/env python3

import sys
import math


def read_numbers(filename: str):
    numbers = []
    with open(filename) as f:
        for line in f:
            try:
                number = float(line)
                numbers.append(number)
            except ValueError:
                pass
    return numbers


def summary(filename: str):
    numbers = read_numbers(filename)
    s = sum(numbers)
    n = len(numbers)
    avg = s / n
    variance = sum((n - avg) ** 2 for n in numbers) / (n - 1)
    stddev = math.sqrt(variance)
    return (s, avg, stddev)


def main():
    for filename in sys.argv[1:]:
        r = summary(filename)
        print(
            f"File: {filename} Sum: {r[0]:.6f} Average: {r[1]:.6f} Stddev: {r[2]:.6f}"
        )


if __name__ == "__main__":
    main()
