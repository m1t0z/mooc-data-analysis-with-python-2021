#!/usr/bin/env python3
from ctypes import ArgumentError
import pandas as pd


def read_series():
    data: list[str] = []
    index: list[str] = []
    while line := input():
        words = line.split()
        if len(words) != 2:
            raise Exception(f"2 words are expected but {len(words)} are given!")

        index.append(words[0])
        data.append(words[1])

    return pd.Series(data, index)


def main():
    print(read_series())


if __name__ == "__main__":
    main()
