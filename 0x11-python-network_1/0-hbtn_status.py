#!/usr/bin/python3

"""
This script fetches status from 'https://alx-intranet.hbtn.io/status'
using urllib package and displays the body of the
response in a formatted manner.
"""

import urllib.request


def fetch_status():
    """
    Fetches status from specified URL and prints body of the response
    """
    url = 'https://alx-intranet.hbtn.io/status'

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        body = response.read()
        utf8_content = body.decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(utf8_content))


if __name__ == "__main__":
    fetch_status()
