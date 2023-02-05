#!/usr/bin/python3

"""
A module that defines a square class.
"""

class Square:
    """
    A class that defines a square.

    Attributes:
    size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize the square with an optional size.

        Args:
        size (int): The size of the square. Defaults to 0.

        Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """int: The size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
        value (int): The size to set for the square.

        Raises:
        TypeError: If the size is not an integer.
        ValueError: If the size is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size ** 2
