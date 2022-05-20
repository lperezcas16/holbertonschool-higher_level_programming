#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request to the passed URL """

import urllib.request
import sys

if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]}).encode()

    req = urllib.request.Request(sys.argv[1], data=data, method="POST")

    with urllib.request.urlopen(req) as respose:
        print(respose.read().decode('utf-8'))
