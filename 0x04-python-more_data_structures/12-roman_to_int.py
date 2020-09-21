#!/usr/bin/python3
def roman_to_int(roman_string):

    my_dicc = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    num = 0

    if roman_string is None or type(roman_string) is not str:
        return 0

    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            num += my_dicc[roman_string[i]]
        elif my_dicc[roman_string[i]] >= my_dicc[roman_string[i + 1]]:
            num += my_dicc[roman_string[i]]
        else:
            num -= my_dicc[roman_string[i]]
    return num

#
# X = 10
# VII = 7
# IX = 9
# LXXXVII = 87
# DCCVII = 707
