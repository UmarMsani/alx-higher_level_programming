#!/usr/bin/python3

"""
This script fetches status from 'https://alx-intranet.hbtn.io/status'
using the requests package and displays the body of the response
in a formatted manner.
"""

import requests


def fetch_status():
    """
    Fetches status from specified URL and prints body of the response.
    """
    url = 'https://alx-intranet.hbtn.io/status'

    response = requests.get(url)

    if response.status_code == 200:
        content = response.text
        print("- Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
    else:
        print(f"Error: {response.status_code}")


if __name__ == "__main__":
    fetch_status()
