#!/usr/bin/python3
"""
read file
"""


def read_file(filename=""):
    """
    read filename
    """
    with open(filename, encoding='UTF8') as f:
        file = f.read()
        print(file, end="")
