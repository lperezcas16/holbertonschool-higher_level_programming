#!/usr/bin/python3
def uppercase(str):
    for count_str in str:
        numb = ord(count_str)
        if numb in range(97, 123):
            numb -= 32
        print("{0}".format(chr(numb)), end='')
    print("")
