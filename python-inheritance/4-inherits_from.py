#!/usr/bin/python3
"""
checks if an object inherited from a specific class
"""


def inherits_from(obj, a_class):
    """
    Returns true if an object inherited from a class
    """
    return isinstance(obj, a_class) and not type(obj) is a_class
