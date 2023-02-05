#!/usr/bin/python3
"""
module that defines a Rectangle
"""


class Rectangle:
    """
    Rectangle class
    """
    def __init__(self, width=0, height=0):
        """
        no error checking yet
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """
        getter for size
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        setter for height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        getter for width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        setter for width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        returns the aree
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        returns the perimeter
        """
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return 2 * self.__height + 2 * self.__width

    def __str__(self):
        """
        returns the rectangle represented by #
        """
        rectangle = ""

        if self.__width == 0 or self.__height == 0:
            return rectangle

        for i in range(self.__height):
            rectangle = rectangle + ("#" * self.width) + "\n"

        return rectangle
