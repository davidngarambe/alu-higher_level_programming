#!/bin/bash
# Script that takes in a URL, sends a GET request, and displays the response body if the status code is 200.
curl -sL -w "%{http_code}" "$1" -o response.txt | grep -q "200" && cat response.txt
