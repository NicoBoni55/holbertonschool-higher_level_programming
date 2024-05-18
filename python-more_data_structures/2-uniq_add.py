#!/usr/bin/python3
def uniq_add(my_list=[]):
    contador = 0
    for numeros in set(my_list):
        contador += numeros
    return contador
