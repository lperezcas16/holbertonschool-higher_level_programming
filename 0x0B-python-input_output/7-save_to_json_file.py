#!/usr/bin/python3
"""OBJ -> txt"""
import json


def save_to_json_file(my_obj, filename):
    """ method OBJ -> txt"""
    with open(filename, 'w+') as fil:
        json.dump(my_obj, fil)
