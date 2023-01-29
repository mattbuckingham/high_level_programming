#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for i, row in enumerate(matrix):
        new_matrix.append([])
        for j, element in enumerate(row):
            new_matrix[i].append(element ** 2)
    return new_matrix
