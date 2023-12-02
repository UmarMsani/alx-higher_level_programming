#!/usr/bin/python3

"""
This script takes a URL and an email as input, sends a POST
request to the URL with the email as a parameter, and displays
the body of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email
    as a parameter and displays the body of the response
    (decoded in utf-8).
    """
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url, data=data, method='POST')

    with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print(body)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
