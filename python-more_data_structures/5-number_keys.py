#!/usr/bin/python3
def number_keys(a_dictionary):
    contador = 0
    for elementos in a_dictionary:
        if elementos in a_dictionary:
            contador += 1
    return contador
