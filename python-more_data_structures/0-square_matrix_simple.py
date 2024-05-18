#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    if matrix:
        for elementos in matrix:
            new_matrix.append(list(map(lambda i: pow(i, 2), elementos)))
    return new_matrix
