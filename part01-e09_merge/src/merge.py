#!/usr/bin/env python3


def merge(L1, L2):
    merged = []
    i1, i2 = (0, 0)
    while i1 < len(L1) and i2 < len(L2):
        if L1[i1] <= L2[i2]:
            merged.append(L1[i1])
            i1 += 1
        else:
            merged.append(L2[i2])
            i2 += 1
    merged += L1[i1:] + L2[i2:]
    return merged


def main():
    print(f"merge([0,1,2], [3,4,5]) = {merge([0,1,2],[3,4,5])}")
    print(f"merge([1,3,5], [2,4,6]) = {merge([0,1,2],[3,4,5])}")
    print(f"merge([], [3,4,5]) = {merge([],[3,4,5])}")
    print(f"merge([0,1,2], []) = {merge([0,1,2],[])}")


if __name__ == "__main__":
    main()
