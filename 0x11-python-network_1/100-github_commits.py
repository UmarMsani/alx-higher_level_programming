#!/usr/bin/python3

"""
This script lists 10 commits (from most recent to oldest) of a specified
repository by a particular user using the GitHub API, requests, and sys.
"""

import requests
import sys


def list_commits(repo_name, owner_name):
    """
    Lists 10 commits (from most recent to oldest) of the specified repository
    by the specified owner using the GitHub API.
    """
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    params = {'per_page': 10}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        commits = response.json()
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Failed to fetch commits. Status code:", response.status_code)


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    list_commits(repo_name, owner_name)
