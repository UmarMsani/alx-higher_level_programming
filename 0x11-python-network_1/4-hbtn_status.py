#!/usr/bin/python3

"""
This script fetches status from 'https://alx-intranet.hbtn.io/status'
using the requests package and displays the body of the response
in a formatted manner.
"""

import requests


if __name__ == "__main__":
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
