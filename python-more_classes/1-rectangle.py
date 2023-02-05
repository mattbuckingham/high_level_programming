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
        self.__height = height
        self.__witdth = width

    @property
    def height(self):
        """
        getter for size
        """
        return self.__height

    @height.setter
    def height(self, ):
        """
        setter for height
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
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
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        return self.__width
