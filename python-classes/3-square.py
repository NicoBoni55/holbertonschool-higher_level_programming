#!/usr/bin/python3
"""Class Square

"""


class Square:
    """
    Esta clase representa un cuadrado

     Atributos:
     size

    Métodos:
    No tiene
    """
    def __init__(self, size=0):
        """__init__

        __init__ inicializa size

        Atributos:
        Size

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """area

        area del cuadrado

        Atributos:
        self

        """
        return pow(self.__size, 2)
