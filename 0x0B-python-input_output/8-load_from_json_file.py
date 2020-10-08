#!/usr/bin/python3
"""json->Object"""
import json


def load_from_json_file(filename):
    """json-> Object"""
    with open(filename, 'r') as file:
        return json.load(file)
