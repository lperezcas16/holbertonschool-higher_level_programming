#!/usr/bin/python3
def remove_char_at(str, n):
    strcpy = ""
    i = 0
    for count_str in str:
        if i != n:
            strcpy = strcpy + count_str
        i += 1
    return (strcpy)
