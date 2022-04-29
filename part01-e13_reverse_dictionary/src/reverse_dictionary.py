#!/usr/bin/env python3
from collections import defaultdict


def reverse_dictionary(d):
    reversed_d = defaultdict(list)
    for k, V in d.items():
        for v in V:
            reversed_d[v].append(k)
    return dict(reversed_d)


def main():
    d = {
        "move": ["liikuttaa"],
        "hide": ["piilottaa", "salata"],
        "six": ["kuusi"],
        "fir": ["kuusi"],
    }
    print(reverse_dictionary(d))


if __name__ == "__main__":
    main()
