#!/usr/bin/python3
"""
same type class
"""


def is_same_class(obj, a_class):
    """
    if obj is exactly an instance of the class return true
    in otherwise return false
    """
    if type(obj) is not a_class:
        return False
    else:
        return True
