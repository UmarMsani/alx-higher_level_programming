#!/usr/bin/python3

"""
This script takes GitHub credentials (username and personal access token)
and uses Basic Authentication with the GitHub API to display the user ID
using requests and sys.
"""

from sys import argv
import requests


if __name__ == "__main__":
    a = (argv[1], argv[2])
    request = requests.get("https://api.github.com/user", auth=a)
    print(request.json().get("id"))
