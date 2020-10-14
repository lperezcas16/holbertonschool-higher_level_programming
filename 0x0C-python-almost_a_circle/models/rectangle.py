#!/usr/bin/python3
""" Rectancle project """
from models.base import Base


class Rectangle(Base):
    """Class Rectangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Contructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """atributes """
        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id,
                    self.x, self.y, self.width, self.height)

    def area(self):
        """ Method return area"""
        return self.width * self.height

    def display(self):
        """print rectangle"""
        for y in range(self.y):
            print()
        for height in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for width in range(self.width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        """Update rectangle class"""
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

    @property
    def width(self):
        """Getter"""
        return self.__width

    @property
    def height(self):
        """Getter"""
        return self.__height

    @property
    def x(self):
        """Getter"""
        return self.__x

    @property
    def y(self):
        """Getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be >0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be >0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value
