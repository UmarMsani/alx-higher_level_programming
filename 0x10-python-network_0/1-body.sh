#!/bin/bash
# This script fetches and displays the body of a response for a 200 status code
curl -sX GET $1 -L
