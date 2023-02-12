#!/usr/bin/python3
"""
Append my first text
"""


def append_write(filename="", text=""):
    """
    Append text
    """
    with open(filename, "a", encoding="utf-8") as myfile:
        return myfile.write(text)
