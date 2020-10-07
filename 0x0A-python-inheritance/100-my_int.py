#!/usr/bin/python3
""" Class MyInit-->inherits from Int """


class MyInt(int):
    """ Class MyInit--> inherits from Int """
    def __init__(self, value):
        self.value = value
    """ equal to different """
    def __eq__(self, other):
        return self.value != other
    """ different to equal"""
    def __ne__(self, other):
        return self.value == other
