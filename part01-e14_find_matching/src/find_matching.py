#!/usr/bin/env python3


def find_matching(L, pattern):
    indices = []
    for i, s in enumerate(L):
        if pattern in s:
            indices.append(i)
    return indices


def main():
    print(find_matching(["sensitive", "engine", "rubbish", "comment"], "en"))


if __name__ == "__main__":
    main()
