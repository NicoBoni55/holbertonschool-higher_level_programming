#!/usr/bin/python3
"""
import pickle
"""
import pickle
"""
pickle
"""


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        imprime los atributos en display
        """
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        serialize
        """
        try:
            with open(filename, "wb") as file:
                pickle.dump(self, file)
        except (TypeError, FileNotFoundError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        deserialize
        """
        try:
            with open(filename, "rb") as file:
                obj = pickle.load(file)
            return obj
        except (TypeError, FileNotFoundError):
            return None
