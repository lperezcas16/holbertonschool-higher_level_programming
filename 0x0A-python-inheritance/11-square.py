#!/usr/bin/python3
"""Class"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Square size"""
        return "[Square] {:d}/{:d}".format(self.__size, self.__size)
