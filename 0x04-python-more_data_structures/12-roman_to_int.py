#!/usr/bin/python3
def roman_to_int(roman_string):
    num = 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    if type(roman_string) is not str or not roman_string:
        return 0

    for i in range(len(roman_string)):
        if i == len(roman_string) - 1:
            num += d[roman_string[i]]
        elif d[roman_string[i]] >= d[roman_string[i + 1]]:
            num += d[roman_string[i]]
        else:
            num -= d[roman_string[i]]

    return num
