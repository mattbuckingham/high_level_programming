#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    def multiply(x):
        return x*number
    return list(map(multiply, my_list))
