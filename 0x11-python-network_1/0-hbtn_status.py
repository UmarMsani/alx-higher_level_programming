#!/usr/bin/python3

"""
This script fetches the status from 'https://alx-intranet.hbtn.io/status'
using urllib package and displays the body of the response in a formatted manner.
"""

import urllib.request

def fetch_status():
    """
    Fetches the status from a specified URL and prints the body of the response.
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
