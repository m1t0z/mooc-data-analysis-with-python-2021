#!/usr/bin/env python3

import re


def red_green_blue(filename="src/rgb.txt"):
    res = []
    with open(filename) as f:
        for line in f:
            match = re.match(r"(\d{0,3})\s+(\d{0,3})\s+(\d{0,3})\s+(.*)", line.strip())
            if match:
                red = match.group(1)
                green = match.group(2)
                blue = match.group(3)
                name = match.group(4)
                res.append(f"{red}\t{green}\t{blue}\t{name}")

    return res


def main():
    results = red_green_blue()
    for res in results:
        print(res)


if __name__ == "__main__":
    main()
