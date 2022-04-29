#!/usr/bin/env python3


def triple(val):
    return val * 3


def square(val):
    return val**2


def main():
    for i in range(10):
        val = i + 1
        trippled = triple(val)
        squared = square(val)
        if squared > trippled:
            break

        print(f"triple({val})=={trippled} square({val})=={squared}")


if __name__ == "__main__":
    main()
