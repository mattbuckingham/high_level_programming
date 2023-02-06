#!/usr/bin/python3
def lookup(obj):
"""
Method that returns a list of all attributes and methods available to obj
"""
    return [dir(obj)]
