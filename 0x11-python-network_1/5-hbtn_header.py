#!/usr/bin/python3

"""
This script takes a URL as input, sends a request to the URL,
and displays the value of the X-Request-Id variable found in the
header of the response using requests and sys.
"""

import requests
import sys


def get_x_request_id(url):
    """
    Sends a request to the specified URL and retrieves the
    value of the X-Request-Id header.
    """
    response = requests.get(url)

    x_request_id = response.headers.get('X-Request-Id')
    if x_request_id:
        print(x_request_id)


if __name__ == "__main__":
    url = sys.argv[1]
    get_x_request_id(url)
