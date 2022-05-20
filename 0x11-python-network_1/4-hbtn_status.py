#!/usr/bin/python3
""" displays info about https://intranet.hbtn.io/status using requests """

import requests


if __name__ == "__main__":
    html = requests.get("https://intranet.hbtn.io/status").text

    print("Body response:")
    print("\t- type:", type(html))
    print("\t- content:", html)
