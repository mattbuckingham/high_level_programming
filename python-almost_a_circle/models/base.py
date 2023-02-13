#!/usr/bin/python3
"""
Base Class
"""


class Base:
    """
    Base Class
    """
    __nb_objects = 0

    def __init__(self, id=None):

        if id is None:
            Base.id = __nb_objects
            __nb_objects += 1
        else:
            self.id = id
