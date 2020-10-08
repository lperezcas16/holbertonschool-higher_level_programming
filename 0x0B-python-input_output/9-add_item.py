#!/usr/bin/python3
""" Project to use two early funcitons """
from sys import argv

load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file

try:
    items = load_from_json_file('add_item.json')
    save_to_json_file(items + argv[1:], 'add_item.json')
except Exception:
    save_to_json_file(argv[1:], 'add_item.json')
