#!/usr/bin/python3
"""
add_integer
"""


def add_integer(a, b=98):
    """
    Return a + b
    function that adds 2 integers
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
