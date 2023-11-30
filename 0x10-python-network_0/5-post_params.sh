#!/bin/bash
# Sends a POST request with specific variables to the provided URL and displays the response body
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
