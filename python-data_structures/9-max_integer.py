#!/usr/bin/python3
def max_integer(my_list=[]):
    max_val = float("-inf")
    for i, value in enumerate(my_list):
        if max_val < value:
            max_val = value
    return max_val
