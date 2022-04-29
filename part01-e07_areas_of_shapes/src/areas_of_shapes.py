#!/usr/bin/env python3

import math


def calc_triangle_area(base: float, height: float):
    return base * height / 2


def calc_rectangle_area(width: float, height: float):
    return width * height


def calc_circle_area(radius: float):
    return math.pi * radius**2


def main():
    while True:
        shape = input("Choose a shape (triangle, rectangle, circle): ")
        if shape == "triangle":
            base = float(input("Give base of the triangle: "))
            height = float(input("Give height of the triangle: "))
            area = calc_triangle_area(base, height)
            print(f"The area is {area}")
        elif shape == "rectangle":
            width = float(input(f"Give width of the rectangle: "))
            height = float(input(f"Give height of the rectangle: "))
            area = calc_rectangle_area(width, height)
            print(f"The area is {area}")
        elif shape == "circle":
            radius = float(input(f"Give radius of the circle: "))
            area = calc_circle_area(radius)
            print(f"The area is {area}")
        elif shape == "":
            break
        else:
            print("Unknown shape!")


if __name__ == "__main__":
    main()
