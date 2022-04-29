#!/usr/bin/env python3


def transform(s1, s2):
    to_ints = lambda s: map(int, s.split())
    return [a * b for a, b in zip(to_ints(s1), to_ints(s2))]


def main():
    print(transform("1 5 3", "2 6 -1"))


if __name__ == "__main__":
    main()
