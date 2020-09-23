#!/usr/bin/python3
""" Class square """


class Square:
    """ function that initialize values """

    def __init__(self, size=0, position=(0, 0)):
        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        if type(position) is not tuple or len(position) != 2\
                or type(position[0]) is not int or type(position[1]) is not int\
                or position[0] < 0 or position[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = position
        self.__size = size

    """ Getter Size"""

    @property
    def size(self):
        return self.__size

    """ Setter Size"""

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """ Getter Position"""

    @property
    def position(self):
        return self.__position

    """ Setter Position"""

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2\
                or type(value[0]) is not int or type(value[1]) is not int\
                or value[0] < 0 or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    """ Getter area """

    def area(self):
        return self.__size ** 2

    """ Print All Aquare"""

    def my_print(self):
        if self.__size > 0:
            for i in range(self.__position[1]):
                print("")
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.__size):
                    print("#", end="")
                print("")
        else:
            print("")
