#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        needed_zeroes = 2 - len(tuple_a)
        tuple_a = tuple_a + tuple(0 for i in range(needed_zeroes))
    if len(tuple_b) < 2:
        needed_zeroes = 2 - len(tuple_b)
        tuple_b = tuple_b + tuple(0 for i in range(needed_zeroes))

    tuple_a = tuple_a[:2]
    tuple_b = tuple_b[:2]

    return (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
