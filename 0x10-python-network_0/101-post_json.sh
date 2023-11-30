#!/bin/bash
# Sends a JSON POST request with the contents of the file in the body and displays the response body
curl -sX POST -d "@$2" -H "Content-Type: application/json" "$1"
