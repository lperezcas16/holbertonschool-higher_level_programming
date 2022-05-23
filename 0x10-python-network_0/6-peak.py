#!/usr/bin/python3
""" finds a peak in a list of unsorted integers. """


def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers.

    Args:
        list_of_integers (list): unsorted list
    """
    if list_of_integers == []:
        return

    list_ = list_of_integers
    l_len = len(list_)
    peak = list_[0]
    i = 0
    while i < l_len:
        if peak < list_[i]:
            peak = list_[i]

        if i < l_len - 1:
            if list_[i] > list_[i + 1]:
                if i == 0:
                    return list_[i]
                if list_[i] > list_[i - 1]:
                    return list_[i]
                i += 1

        i += 1

    return peak
