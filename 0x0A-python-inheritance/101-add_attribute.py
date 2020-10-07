#!/usr/bin/python3
""" Adds a new attribute to an object """


def add_attribute(obj, name, value):
    """ Adds a new attribute to an object """
    if hasattr(obj, '__dict__') is False:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
