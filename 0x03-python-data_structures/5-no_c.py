#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for counter in my_string:
        if counter != 'c' and counter != 'C':
            new += counter
    return new
