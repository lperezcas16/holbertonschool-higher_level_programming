#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":

    leng = len(argv)
    mult_ar = "arguments"

    if leng == 1:
        print("0 {}.".format(mult_ar))
    elif leng == 2:
        print("{} argument:".format(leng - 1))
        print("1: {}".format(argv[1]))
    else:
        print("{} {}:".format(leng - 1, mult_ar))
        for count in range(1, leng):
            print("{}: {}".format(count, argv[count]))
