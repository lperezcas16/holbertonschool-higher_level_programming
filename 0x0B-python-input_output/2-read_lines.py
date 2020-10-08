#!/usr/bin/python3
"""Read n line of a txt"""
number_of_lines = __import__("1-number_of_lines"). number_of_lines


def read_lines(filename="", nb_lines=0):
    """method read lines"""
    with open(filename, 'r') as file:
        if nb_lines <= 0 or nb_lines > number_of_lines(filename):
            nb_lines = number_of_lines(filename)
        for i in range(nb_lines):
            print(file.readline(), end='')
