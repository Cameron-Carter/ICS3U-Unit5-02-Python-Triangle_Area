#!/usr/bin/env python3

# Created by: Cameron Carter
# Created on May 2021
# This program finds the area of a triangle

import string


def find_area(base, height):
    # Finds area

    # Process and output
    area = (base * height) / 2
    print("The area of the triangle is {} cm².".format(area))


def main():
    # This function calls find_area

    # Input
    base_as_string = str(input("Enter the base length in cm: "))
    height_as_string = str(input("Enter the height in cm: "))

    # Process and output
    try:
        base_as_float = float(base_as_string)
        height_as_float = float(height_as_string)
        if base_as_float > 0 and height_as_float > 0:
            find_area(base_as_float, height_as_float)  # Call find_area
        else:
            print("Invalid dimensions.")
    except Exception:
        print("Invalid dimensions.")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
