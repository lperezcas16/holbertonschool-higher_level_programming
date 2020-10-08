#!/usr/bin/python3
"""Read number lines"""


def number_of_lines(filename=""):
    """read method"""
    with open(filename, encoding='utf8') as file:
        i = 0
        for line in file:
            i += 1
        return i
