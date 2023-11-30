#!/bin/bash
# Sends a request to cause the server to respond with a message
curl -s -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin:HolbertonSchool"
