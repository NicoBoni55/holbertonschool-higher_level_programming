#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for letras in my_string:
        if letras != 'c' and letras != 'C':
            new_string += letras
    return new_string
