#!/bin/bash
# sends a request and displays only the status code of the response.
curl $1 -w %{http_code} -so nul
