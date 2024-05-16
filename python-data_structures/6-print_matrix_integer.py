#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        i = 1
        for y in x:
            if (i == len(x)):
                print("{:d}".format(y), end="\n")
            else:
                print("{:d}".format(y), end=" ")
            i += 1
