#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sort_dir = sorted(a_dictionary.keys())
    for j in sort_dir:
        print("{}: {}".format(j, a_dictionary[j]))
