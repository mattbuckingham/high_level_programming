#!/usr/bin/python3
"""
Read my first fiel
"""


def read_file(filename=""):
    """
    Read File
    """
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read(), end="")
