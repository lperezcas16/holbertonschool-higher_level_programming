#!/usr/bin/python3
""" displays the value of the X-Request-Id variable """

import requests
import sys

if __name__ == "__main__":
    reply = requests.get(sys.argv[1])
    print(reply.headers.get("X-Request-Id"))
