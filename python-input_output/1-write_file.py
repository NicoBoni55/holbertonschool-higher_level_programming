#!/usr/bin/python3
"""
write file
"""


def write_file(filename="", text=""):
    """
    write file
    """

    with open(filename, encoding='UTF8') as f:
        return (len(f.write(text)))