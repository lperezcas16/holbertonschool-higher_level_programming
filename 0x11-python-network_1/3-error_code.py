#!/usr/bin/python3
""" displays info about https://intranet.hbtn.io/status """

import urllib.request
import sys

if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as respose:
            print(respose.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)
