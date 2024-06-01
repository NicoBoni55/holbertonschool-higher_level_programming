#!/usr/bin/python3
"""
student
"""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_d = {}
        diccionario = self.__dict__
        if type(attrs) is list:
            for elementos in attrs:
                if type(elementos) is str:
                    if elementos in diccionario:
                        new_d[elementos] = diccionario[elementos]
            return new_d
        else:
            return diccionario
