#!/usr/bin/env python3

# Don't modify the below hack
try:
    from src import triangle
except ModuleNotFoundError:
    import triangle


def main():
    print("hypothenuse (a=3,b=5): ", triangle.hypothenuse(3, 4))
    print("area (10,10)", triangle.area(10, 10))


if __name__ == "__main__":
    main()
