#!/usr/bin/env python3


def extract_numbers(s: str):
    numbers = []
    for token in s.split():
        try:
            numbers.append(int(token))
        except ValueError:
            try:
                numbers.append(float(token))
            except ValueError:
                pass

    return numbers


def main():
    print(extract_numbers("abd 123 1.2 test 13.2 -1"))


if __name__ == "__main__":
    main()
