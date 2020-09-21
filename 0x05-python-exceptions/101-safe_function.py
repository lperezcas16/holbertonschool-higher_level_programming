#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        res = fct(*args)
    except Exception as err:
        res = None
        print("Exception:", err, file=sys.stderr)

    return res
