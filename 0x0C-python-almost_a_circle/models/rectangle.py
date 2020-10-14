#!/usr/bin/python3
""" Rectancle project """
from models.base import Base


class Rectangle(Base):
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

    """Getter"""
    @property
    def width(self):
        return self.__width
    """Getter"""
    @property
    def height(self):
        return self.__height
    """Getter"""
    @property
    def x(self):
        return self.__x
    """Getter"""
    @property
    def y(self):
        return self.__y

    """Setter"""
    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >0")
        self.__width = value
    """Setter"""
    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >0")
        self.__height = value
    """Setter"""
    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value
    """Setter"""
    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value
