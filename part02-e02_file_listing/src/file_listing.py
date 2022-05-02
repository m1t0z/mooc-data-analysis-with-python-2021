#!/usr/bin/env python3

import re


def file_listing(filename="src/listing.txt"):

    reo = re.compile(
        r"^.{10}\s+\d+\s+\S+\s+\S+\s+(\d+)\s+([a-zA-Z]+)\s+(\d{1,2})\s+(\d{2}):(\d{2})\s+(\S+)\s*$"
    )

    res = []
    with open(filename) as f:
        for line in f:
            m = reo.match(line)
            if m:
                size = int(m.group(1))
                month = m.group(2)
                day = int(m.group(3))
                hour = int(m.group(4))
                minute = int(m.group(5))
                name = m.group(6)
                res.append((size, month, day, hour, minute, name))
    return res


def main():
    print(file_listing())


if __name__ == "__main__":
    main()
