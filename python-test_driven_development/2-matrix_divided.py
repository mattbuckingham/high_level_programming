#!/usr/bin/python3
"""
Module divides all elements of a matrix
"""


def matrix_divided(matrix, div):
    """
    function that divides all elements of a matrix
    """

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisonError("division by zero")
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if type(elem) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists)\
 of integers/floats")

    return [[round(elem/div, 2) for elem in row] for row in matrix]
