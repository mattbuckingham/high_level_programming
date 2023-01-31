#!/usr/bin/python3
"""A class that defines a square"""


class Square:
    """a square"""
    def __init__(self, size=0):
        """ Initialise a new square"""

        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """calculate the area of a square"""
        return self.__size * self.__size
