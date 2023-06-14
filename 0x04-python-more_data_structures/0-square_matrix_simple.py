#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()
    new_matrix = [[x * x for x in row] for row in new_matrix]
    return new_matrix
