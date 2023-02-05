#!/usr/bin/python3
"""
A module that defines a square class.
"""


class Square:
    """
    Square class
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Raises a TyeError error if the size or position is not an int
        Raises a ValueError if the sizeor position is less than 0
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

        if (\
            type(position) != tuple or\
            len(position) != 2 or\
            type(position[0]) != int or\
            type(position[1]) != int or\
            position[0] < 0 or\
            position[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    @property
    def size(self):
        """
        getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        setter for size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        getter for position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        setter for position
        """
        if (\
            type(value) != tuple or\
            len(value) != 2 or\
            type(value[0]) != int or\
            type(value[1]) != int or\
            value[0] < 0 or\
            value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """
        return the area of a square
        """
        return self.__size ** 2

    def my_print(self):
        """
        prints in stdo tthe square with the character #
        """
        if self.size == 0:
            print()
        else:
            print("\n" * self.position[1], end="")
            for i in range(self.size):
                print(" " * self.position[0] + "#" * self.size)
