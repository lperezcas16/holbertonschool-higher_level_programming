#!/usr/bin/python3
"""Class"""


class BaseGeometry:
    """Class base geometry"""

    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be > 0".format(name))
    """Method validate X and Y"""

    def integer_validator2(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value < 0:
            raise ValueError("{} must be >= 0".format(name))
