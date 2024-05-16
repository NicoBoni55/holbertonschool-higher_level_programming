#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        for y in x:
            if (y != 3 or y != 6 or y != 9):
                print("{:d}".format(y), end=" ")
            if (y == 3 or y == 6 or y == 9):
                print(' ')
