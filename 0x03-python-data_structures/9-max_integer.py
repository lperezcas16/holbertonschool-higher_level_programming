#!/usr/bin/python3
def max_integer(my_list=[]):
    if  my_list is None or len(my_list) <= 0:
        return None
    my_list.sort()
    return my_list[-1]
--
