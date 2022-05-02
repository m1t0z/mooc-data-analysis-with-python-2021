#!/usr/bin/env python3


class Prepend:
    def __init__(self, prefix: str) -> None:
        self.start = prefix

    def write(self, what: str) -> None:
        print(f"{self.start}{what}")


def main():
    p = Prepend("+++ ")
    p.write("Hello")


if __name__ == "__main__":
    main()
