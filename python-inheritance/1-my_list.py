#!/usr/bin/python3
"""
Sorts a list
"""


class MyList(list):
    """
    Sorts a list
    """

    def print_sorted(self):
        """
        method to sort a list
        """
        temp_list = sorted(self)
        print(temp_list)
