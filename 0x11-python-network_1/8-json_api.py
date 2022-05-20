#!/usr/bin/python3
""" searchs """
import requests
import sys


data = {"q": ""}

if len(sys.argv) == 2:
    data["q"] = sys.argv[1]

try:
    req = requests.post("http://0.0.0.0:5000/search_user", data=data)

    dict_req = req.json()
    if dict_req == {}:
        print("No result")
    else:
        print("[{}] {}".format(dict_req.get("id"), dict_req.get("name")))
except:
    print("Not a valid JSON")
