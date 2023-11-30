#!/bin/bash
# Sends a GET request with a custom header to the provided URL and displays the response body
curl -s -X GET -H "X-School-User-Id: 98" "$1"
