#!/usr/bin/python3
"""
matrix_divided
"""


def matrix_divided(matrix, div):
    """
    divided a matrix
    """
    new_matrix = []
    message_type = "matrix must be a matrix (list of lists) of integers/floats"
    message_type2 = "Each row of the matrix must have the same size"
    fila_inicial = len(matrix[0])
    if matrix:
        for filas in matrix:
            if len(filas) != fila_inicial:
                raise TypeError(message_type2)
            for elementos in filas:
                if type(div) not in (int, float):
                    raise TypeError("div must be a number")
                if div == 0:
                    raise ZeroDivisionError("division by zero")
                if type(elementos) not in (int, float):
                    raise TypeError(message_type)
            new = [round((elementos) / div, 2) for elementos in filas]
            new_matrix.append(new)
    return new_matrix
