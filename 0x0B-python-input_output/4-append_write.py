#!/usr/bin/python3
"""appends a string at the end of txt"""


def append_write(filename="", text=""):
    """append to the txt"""
    with open(filename, 'a+') as file:
        return file.write(text)
