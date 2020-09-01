#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last = abs(number) % 10
str1 = "Last digit of"
if number < 0:
    last *= -1

if last < 6:
    print("{} {:d} is {:d} and is less than 6 and not 0"
          .format(str1, number, last))
elif last == 0:
    print("{} {:d} is {:d} and is 0"
          .format(str1, number, last))
elif last > 5:
    print("{} {:d} is {:d} and is greater than 5"
          .format(str1, number, last))
