#!/usr/bin/python3
"""
append file
"""


def append_write(filename="", text=""):
    """
    append file
    """
    with open(filename, 'a', encoding='UTF8') as f:
        return f.write(text)
