#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resultado = []
    for numeros in my_list:
        if numeros % 2 == 0:
            resultado.append(True)
        else:
            resultado.append(False)
    return resultado
