#!/usr/bin/python3
"""
write file
"""


def write_file(filename="", text=""):
    """
    write file
    """

    with open(filename, 'w', encoding='UTF8') as f:
        return f.write(text)
