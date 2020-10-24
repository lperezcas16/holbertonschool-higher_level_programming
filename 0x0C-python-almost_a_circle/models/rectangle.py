#!/usr/bin/python3
""" Rectancle project """
from models.base import Base


class Rectangle(Base):
    """[this class create rectangles]

    Args:
        Base ([class]): [inherits from that class]
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """[Contructor]

        Args:
            width ([int]): [width of the rectangle]
            height ([int]): [height if the rectangle]
            x (int, optional): [position in x of the rectangle]. Defaults to 0.
            y (int, optional): [position in y of the rectangle]. Defaults to 0.
            id ([int], optional): [from the Base class]. Defaults to None.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """[toString of Rectangle]

        Returns:
            [text]: [show the atributes of the rectangle]
        """
        return '[Rectangle] ({}) {}/{} - {}/{}'\
            .format(self.id,
                    self.x, self.y, self.width, self.height)

    def area(self):
        """[multipli width and height for the area]

        Returns:
            [int]: [area of the rectangle]
        """
        return self.width * self.height

    def display(self):
        """[printd the rectangle in console]
        """
        for y in range(self.y):
            print()
        for height in range(self.height):
            for x in range(self.x):
                print(" ", end="")
            for width in range(self.width):
                print('#', end="")
            print()

    def update(self, *args, **kwargs):
        """[update the Rectangle class]
        """
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
        """[from object to dictionary]

        Returns:
            [dictionary]: [the created dictionary]
        """
        return {'x': self.x,
                'width': self.width,
                'id': self.id,
                'height': self.height,
                'y': self.y}

    @property
    def width(self):
        """[width getter]

        Returns:
            [int]: [value of width]
        """
        return self.__width

    @property
    def height(self):
        """[height getter]

        Returns:
            [int]: [value of height]
        """
        return self.__height

    @property
    def x(self):
        """[getter x]

        Returns:
            [int]: [value of x]
        """
        return self.__x

    @property
    def y(self):
        """[getter of y]

        Returns:
            [int]: [y value]
        """
        return self.__y

    @width.setter
    def width(self, value):
        """[setter summary]

        Args:
            value ([int]): [the width of the rectangle]

        Raises:
            TypeError: [if the value is not an integer]
            ValueError: [if the value is less or equals to 0]
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """[setter of height]

        Args:
            value ([int]): [the height of the rectangle]

        Raises:
            TypeError: [if the value is not an integer]
            ValueError: [if the value is less or equals to 0]
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """[setter of x]

        Args:
            value ([int]): [position in x]

        Raises:
            TypeError: [verify if x is not an integer]
            ValueError: [verify is x is less to 0]
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """[setter of y]

        Args:
            value ([int]): [The position in y]

        Raises:
            TypeError: [if y is not an integer]
            ValueError: [if y is less 0]
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
