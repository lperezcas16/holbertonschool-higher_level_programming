#!/usr/bin/python3
"""the object is an instance of a class that inherited"""


def inherits_from(obj, a_class):
    """Function"""
    if type(obj) != a_class:
        return isinstance(obj, a_class)
    return False
