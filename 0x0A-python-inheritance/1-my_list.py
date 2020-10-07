#!/usr/bin/python3
""" Class """


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """print sorted list"""
        print(sorted(self))
