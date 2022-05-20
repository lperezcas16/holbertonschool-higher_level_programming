#!/usr/bin/python3
""" displays the content or the status code """

import requests
import sys

if __name__ == "__main__":
    reply = requests.get(sys.argv[1])

    if reply.status_code >= 400:
        print("Error code:", reply.status_code)
    else:
        print(reply.text)
