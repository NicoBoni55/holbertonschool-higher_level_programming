#!/usr/bin/python3
"""
define a rectangle class
"""


class Rectangle:
    """
    define class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """__init__

        __init__ inicializa size
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if (width) < 0:
            raise ValueError("width must be >= 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if (height) < 0:
            raise ValueError("height must be >= 0")
        type(self).number_of_instances += 1
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
        self.__width = value

    @height.setter
    def height(self, value):
        self.__height = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        print_rect = []
        if self.__width == 0 or self.__height == 0:
            self.perimeter = 0
            return ("")
        for altura in range(self.__height):
            for base in range(self.__width):
                print_rect.append(str(self.print_symbol))
            if altura != self.__height - 1:
                print_rect.append("\n")
        return ("".join(print_rect))

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
