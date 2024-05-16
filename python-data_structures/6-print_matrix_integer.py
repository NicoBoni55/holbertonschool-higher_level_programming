#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for x in matrix:
            lista = 1
            for y in x:
                if (lista == len(x)):
                    print("{:d}".format(y), end="")
                else:
                    print("{:d}".format(y), end=" ")
                lista = lista + 1
            print("")
