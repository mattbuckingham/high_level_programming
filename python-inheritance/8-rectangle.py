#!/usr/bin/python3
"""
Class for a rectangle object
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry)

class Rectangle(BaseGeomerty):
    """
    Rectangle object
    """
    def __init__(self, width, height):

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
