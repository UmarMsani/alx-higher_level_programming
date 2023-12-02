#!/usr/bin/python3

"""
This script takes a URL as input, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
It handles urllib.error.HTTPError exceptions.
"""

import urllib.request
import urllib.error
import sys


def fetch_url(url):
    """
    Sends a request to the specified URL and displays the body
    of the response.
    Handles urllib.error.HTTPError exceptions.
    """
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_url(url)
