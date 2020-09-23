#!/usr/bin/python3
""" Class square """


class Square:
    """ Initialize"""

    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    """Define square area """

    def area(self):
        area = self.__size ** 2
        return area

    """ Getter"""
    @property
    def size(self):
        return self.__size

    """ Setter"""
    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    """ print square"""

    def my_print(self):
        if self.__size == 0:
            print('')
            return
        for i in range(self.__size):
            print('#' * self.__size)
