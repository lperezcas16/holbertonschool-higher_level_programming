#!/usr/bin/python3
""" Rectancle project """
from models.base import Base
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(Base, BaseGeometry):
    """Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id,
                    self.x, self.y, self.width, self.height)

    """ Methods"""

    def area(self):
        return self.width * self.height

    def display(self):
        for y in range(self.y):
            print()
        for height in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for width in range(self.width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        if len(args):
            key = ['id', 'width', 'height', 'x', 'y']
            idx = 0
            for value in args:
                if idx < 5:
                    setattr(self, key[idx], value)
                    idx += 1
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Obj -> DIC"""
        return {'x': self.x,
                'width': self.width,
                'id': self.id,
                'height': self.height,
                'y': self.y}

    """Getters"""
    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    """Setters"""
    @width.setter
    def width(self, value):
        self.integer_validator("width", value)
        self.__width = value

    @height.setter
    def height(self, value):
        self.integer_validator("height", value)
        self.__height = value

    @x.setter
    def x(self, value):
        self.integer_validator2("x", value)
        self.__x = value

    @y.setter
    def y(self, value):
        self.integer_validator2("y", value)
        self.__y = value
