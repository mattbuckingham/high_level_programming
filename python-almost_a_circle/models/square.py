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

    def update(self, *args, **kwargs):
        """
        assign arguments to each attribute
        """
        if args:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.size = args[1]
            if num_args >= 3:
                self.x = args[2]
            if num_args >= 4:
                self.y = args[3]
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def to_dictionary(self):
        """
        returns the square as a dict
        """
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}

    def __str__(self):
        """
        replace the __str_ method to return a string
        representation of the square
        """
        return "[Square] ({}) {}/{} - {}"\
            .format(self.id, self.x, self.y, self.height)
