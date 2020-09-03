#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    sum = 0

    for count in argv[1:]:
        sum += int(count)
    print("{}".format(sum))
