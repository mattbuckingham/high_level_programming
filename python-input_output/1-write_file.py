#!/usr/bin/python3
"""
Write my first text
"""


def write_file(filename="", text=""):
    """
    Write text
    """
    with open(filename, encoding="utf-8") as myfile:
        return myfile.write(text)
