#!/usr/bin/python3
"""Class Read file"""


def read_file(filename=""):
    """Read a file (UTF)"""
    with open(filename, 'r') as file:
        print(file.read(), end='')
