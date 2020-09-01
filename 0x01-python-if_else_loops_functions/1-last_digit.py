#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = number % 10
last *= -1
str1 = 'Last digit of'
if last < 0:
    print("{} {:d} is {:d} and is less than 6 and not 0".format(str1, number, last))
elif last == 0:
    print("{} {:d} is {:d} and is 0".format(str1, number, last))
else:
    print("{} {:d} is {:d} and is greater than 5".format(str1, number, last))
