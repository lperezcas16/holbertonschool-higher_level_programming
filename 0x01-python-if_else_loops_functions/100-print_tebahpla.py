#!/usr/bin/python3
for i in range(122, 96, -1):
    if i % 2 == 0:
        print("{0}".format(chr(i)), end='')
    else:
        print("{0}".format(chr(i - 32)), end='')
