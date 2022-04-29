#!/usr/bin/env python3


def _append_range(ranges, r):
    if r[0] == r[1]:
        ranges.append(r[0])
    else:
        ranges.append((r[0], r[1] + 1))


def detect_ranges(L):
    if len(L) == 0:
        return []

    L_sorted = sorted(L)
    r = [L_sorted[0], L_sorted[0]]
    ranges = []
    for el in L_sorted[1:]:
        if r[1] + 1 == el:
            r[1] = el
        else:
            _append_range(ranges, r)
            r[0] = el
            r[1] = el
    _append_range(ranges, r)

    return ranges


def main():
    L = [2, 5, 4, 8, 12, 6, 7, 10, 13]
    result = detect_ranges(L)
    print(L)
    print(result)


if __name__ == "__main__":
    main()
