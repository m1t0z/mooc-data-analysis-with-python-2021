#!/usr/bin/env python3


def main():
    L = [(i, j) for j in range(1, 7) for i in range(1, 7) if i + j == 5]
    print(*L, sep="\n")


if __name__ == "__main__":
    main()
