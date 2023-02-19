#!/usr/bin/python3
"""
Rectangle Class
"""

from models.base import Base


class Rectangle(Base):
    """
    Rectangle Class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        width getter
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        width setter
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        height getter
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        height setter
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        x getter
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        x setter
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        y getter
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        y setter
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        return the area of a recangle
        """
        return (self.__width * self.__height)

    def display(self):
        """
        print the rectangle represented by #
        """
        rectangle = ""

        if self.__width == 0 or self.__height == 0:
            return

        for i in range(self.__y):
            rectangle = rectangle + "\n"
        for j in range(self.__height):
            rectangle = rectangle + (' ' * self.__x)+("#" * self.__width)+"\n"

        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """
        assign arguments to each attribute
        """
        if args:
            num_args = len(args)
            if num_args >= 1:
                self.id = args[0]
            if num_args >= 2:
                self.width = args[1]
            if num_args >= 3:
                self.height = args[2]
            if num_args >= 4:
                self.x = args[3]
            if num_args >= 5:
                self.y = args[4]
        else:
            for arg in kwargs:
                setattr(self, arg, kwargs.get(arg))

    def __str__(self):
        """
        replace the __str_ method to return a string
        representation of the rectangle
        """
        return "[Rectangle] ({}) {}/{} - {}/{}"\
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
