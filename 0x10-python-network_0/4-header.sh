#!/bin/bash
# sends a GET request to the URL, and displays the body of the response
curl -s -X GET -H "X-HolbertonSchool-User-Id: 98" $1
