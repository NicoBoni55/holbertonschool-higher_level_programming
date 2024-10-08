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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area

        area del cuadrado

        Atributos:
        self

        """
        return pow(self.__size, 2)

    def my_print(self):
        """
        imprimir el caracter #
        """
        if self.__size == 0:
            print ("")
        for element in range(self.__size):
            print ("#" * self.__size)
        
