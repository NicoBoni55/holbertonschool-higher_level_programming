#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    maximo = my_list[0]
    for numeros in range(len(my_list)):
        if my_list[numeros] > maximo:
            maximo = my_list[numeros]
    return maximo
