#!/usr/bin/python3
"""Class"""


class BaseGeometry:
    """Class base geometry"""
    def area(self):
        raise Exception("area() is not implemented")

    """Validate as positive number"""
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
