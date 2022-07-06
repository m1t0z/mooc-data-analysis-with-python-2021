#!/usr/bin/env python3
import pandas as pd


def create_series(L1, L2):
    index = list("abc")
    s1 = pd.Series(L1, index)
    s2 = pd.Series(L2, index)
    return (s1, s2)


def modify_series(s1: pd.Series, s2: pd.Series):
    s1_modified = s1.copy()
    s2_modified = s2.copy()
    s1_modified["d"] = s2_modified["b"]
    del s2_modified["b"]
    return (s1_modified, s2_modified)


def main():
    s1, s2 = create_series([0, 1, 2], [3, 4, 5])
    s1.name = "s1"
    s2.name = "s2"
    print(s1)
    print(s2)

    s1_modified, s2_modified = modify_series(s1, s2)
    s1_modified.name = "s1_modified"
    s2_modified.name = "s2_modified"
    print(s1_modified)
    print(s2_modified)

    s_modified_sum = s1_modified + s2_modified
    s_modified_sum.name = "s1_modified + s2_modified"
    print(s_modified_sum)


if __name__ == "__main__":
    main()
