#!/usr/bin/python3
"""get the titles of subreddit"""


import requests


def top_ten(subreddit):
    """return the first 10 hot posts for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    response = requests.get(url=url, allow_redirects=False, headers=headers)
    if response == 404:
        return None

    data = response.json().get("children")
    for item in data:
        print(item.get("title"))
