#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list[:]
    for data, num in enumerate(my_list):
        if num == search:
            new_list[data] = replace
    return new_list
