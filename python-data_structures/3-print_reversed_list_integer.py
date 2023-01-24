#!/usr/bin/python3


def print_reversed_list_integer_recursion(idx, my_list=[]):
    if idx == 0:
        return
    print("{:d}".format(my_list[(idx-1)]))
    print_reversed_list_integer_recursion(idx - 1, my_list)

def print_reversed_list_integer(my_list=[]):
    print_reversed_list_integer_recursion(len(my_list), my_list)
