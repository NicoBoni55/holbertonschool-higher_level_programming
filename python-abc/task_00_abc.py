#!/usr/bin/python3
"""
task 00
"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """
    define class
    """

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    """
    define class
    """

    def sound(self):
        return "Bark"


class Cat(Animal):
    """
    define class
    """

    def sound(self):
        return "Meow"
