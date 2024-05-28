#!/usr/bin/python3
"""
write file
"""


def write_file(filename="", text=""):
    """
    write file
    """
    contador = 0
    with open(filename, encoding='UTF8') as f:
        for line in f:
            contador += 1
    return contador
