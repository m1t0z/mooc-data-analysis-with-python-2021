#!/usr/bin/env python3


def interleave(*lists):
    res = []
    for t in zip(*lists):
        res.extend(t)
    return res


def main():
    print(interleave([1, 2, 3], [20, 30, 40], ["a", "b", "c"]))


if __name__ == "__main__":
    main()
