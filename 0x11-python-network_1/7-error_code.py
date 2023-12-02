#!/usr/bin/python3

"""
This script takes a URL as input, sends a request to the URL, and
displays the body of the response. If the HTTP status code is
greater than or equal to 400, it prints an error message with the
HTTP status code using requests and sys.
"""

import requests
import sys


def fetch_url(url):
    """
    Sends a request to the specified URL and displays the body of
    the response.
    If HTTP status code >= 400, prints an error message.
    """
    response = requests.get(url)

    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_url(url)
