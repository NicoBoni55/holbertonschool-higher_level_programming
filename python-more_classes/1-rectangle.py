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
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if type(value) is not int:
            raise TypeError("height must be an integer")
        self.__width = value

    @height.setter
    def height(self, value):
        if (value) < 0:
            raise ValueError("width must be >= 0")
        if (value) < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
