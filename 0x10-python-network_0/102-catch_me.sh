#!/bin/bash
# makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!
curl -s -X PUT 0.0.0.0:5000/catch_me_3 -H "Origin: HolbertonSchool"
