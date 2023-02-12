#!/usr/bin/python3
"""
Class for a rectangle object
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Rectangle object
    """
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

class Square(Rectangle):
    """
    Square Object
    """
    def __init__(self, size):

        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self._size ** 2
