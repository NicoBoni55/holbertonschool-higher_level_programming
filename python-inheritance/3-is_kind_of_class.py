#!/usr/bin/python3
"""
same class
"""


def is_kind_of_class(obj, a_class):
    """
    is the same class or inherited
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
