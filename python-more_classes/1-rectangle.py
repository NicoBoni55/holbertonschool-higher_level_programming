#!/usr/bin/python3
"""
define a rectangle class
"""


class Rectangle:
    """
    define class
    """
    def __init__(self, width=0, height=0):
        """__init__

        __init__ inicializa size
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if (width) < 0:
            raise ValueError("width must be >= 0")
        if (height) < 0:
            raise ValueError("height must be >= 0")
        self.width = width
        self.height = height
