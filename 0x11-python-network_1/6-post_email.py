#!/usr/bin/python3

"""
This script takes a URL and an email address as input, sends
a POST request to the URL with the email as a parameter, and
displays the body of the response using requests and sys.
"""

import requests
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with the email as a
    parameter and displays the body of the response.
    """
    data = {'email': email}
    response = requests.post(url, data=data)

    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    send_post_request(url, email)
