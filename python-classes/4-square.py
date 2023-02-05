#!/usr/bin/python3
"""defines a square class"""


class Square:
    """Square class"""
    def __init__(self, size=0):
        """
        raises a TyeError error if the size is not an int
        raises a ValueError if the size is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        else self.__size = size

    @property
    def size(self):
        """getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        else self.__size =  value

    def area(self):
        """return the area of a square"""
        return self.__size ** 2
