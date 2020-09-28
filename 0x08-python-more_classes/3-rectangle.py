#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    def __init__(self, widht=0, height=0):
        self.width = widht
        self.height = height

    """Getters"""

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    """Setters"""

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    """Functions"""

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.width + self.height)

    """ toString"""

    def __str__(self):
        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        for i in range(self.__height):
            for j in range(self.__width):
                rect += '#'
            if (i < self.__height - 1):
                rect += '\n'
        return rect
