#!/usr/bin/python3
"""
Prints a square using #
"""


def print_square(size):
    """
    Print a square
    """

    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not int:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size + "\n")
