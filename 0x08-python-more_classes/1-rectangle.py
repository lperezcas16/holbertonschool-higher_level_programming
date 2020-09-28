#!/usr/bin/python3
""" Rectangle class """


class Rectangle:
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    """ GetterS """

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    """ Setters """
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
            raise ValueError("height must be a >= 0")
        self.__height = value
