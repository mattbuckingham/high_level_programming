#!/usr/bin/python3
"""
checks if an object is or inherited from a specific class
"""


def is_kind_of_class(obj, a_class):
    """
    Returns true if an object is or inherited from a class
    """
    return isinstance(obj, a_class)
