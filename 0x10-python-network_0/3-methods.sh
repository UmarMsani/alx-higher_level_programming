#!/bin/bash
# Displays the allowed HTTP methods for the provided URL
curl -sI "$1" | grep -i allow | cut -d ' ' -f 2-
