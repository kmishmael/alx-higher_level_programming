#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col in row:
            print("{:d}".format(col), end = '' if row.index(col) == len(row) - 1 else ' ')
        print()