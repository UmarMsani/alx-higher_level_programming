#!/usr/bin/python3

"""
This script takes a URL as input, sends a request to the URL,
and displays the value
of the X-Request-Id variable found in header of the response
"""

import urllib.request
import sys


def get_x_request_id(url):
    """
    Sends request to specified URL & retrieves value of X-Request-Id header.
    """
    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print(x_request_id)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
