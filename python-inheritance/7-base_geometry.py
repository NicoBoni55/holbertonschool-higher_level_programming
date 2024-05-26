#!/usr/bin/python3
"""
base_geometry
"""


class BaseGeometry():
    """
    geometry class
    """

    def area(self):
        """
        define area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        integer validator
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
