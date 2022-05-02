#!/usr/bin/env python3


class Rational:
    def __init__(self, numenator: int, denominator: int) -> None:
        self.numenator = numenator
        self.denominator = denominator

    def __mul__(self, other: "Rational") -> "Rational":
        return Rational(
            self.numenator * other.numenator, self.denominator * other.denominator
        )

    def __truediv__(self, other: "Rational") -> "Rational":
        return self * Rational(other.denominator, other.numenator)

    def __add__(self, other: "Rational") -> "Rational":
        return Rational(
            self.numenator * other.denominator + other.numenator * self.denominator,
            self.denominator * other.denominator,
        )

    def __sub__(self, other: "Rational") -> "Rational":
        return Rational(
            self.numenator * other.denominator - other.numenator * self.denominator,
            self.denominator * other.denominator,
        )

    def __float__(self) -> float:
        return self.numenator / self.denominator

    def __lt__(self, other: "Rational") -> bool:
        return self.numenator * other.denominator < other.numenator * self.denominator

    def __gt__(self, other: "Rational") -> bool:
        return self.numenator * other.denominator > other.numenator * self.denominator

    def __eq__(self, other: "Rational") -> bool:
        return self.numenator * other.denominator == other.numenator * self.denominator

    def __str__(self) -> str:
        return f"{self.numenator}/{self.denominator}"


def main():
    r1 = Rational(1, 4)
    r2 = Rational(2, 3)
    print(r1)
    print(r2)
    print(r1 * r2)
    print(r1 / r2)
    print(r1 + r2)
    print(r1 - r2)
    print(Rational(1, 2) == Rational(2, 4))
    print(Rational(1, 2) > Rational(2, 4))
    print(Rational(1, 2) < Rational(2, 4))


if __name__ == "__main__":
    main()
