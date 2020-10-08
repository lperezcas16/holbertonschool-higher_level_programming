#!/usr/bin/python3
"""Write file class"""


def write_file(filename="", text=""):
    """Method write file"""
    with open(filename, 'w+') as file:
        return file.write(text)
