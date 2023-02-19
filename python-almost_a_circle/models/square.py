#!/usr/bin/python3
"""
Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square
    """
    def __init__(self, size, x=0, y=0, id=None):

        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        """
            Size Getter
        """
        return self.width

    @size.setter
    def size(self, value):
        """
            Size Setter
        """
        self.width = value
        self.height = value

    def __str__(self):
        """
        replace the __str_ method to return a string
        representation of the square
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)
