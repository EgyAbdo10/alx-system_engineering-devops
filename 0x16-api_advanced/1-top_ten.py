#!/usr/bin/python3
"""get the titles of subreddit"""


import requests


def top_ten(subreddit):
    """return the first 10 hot posts for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": 10}
    response = requests.get(url=url, allow_redirects=False,
                            headers=headers, params=params)
    if response == 404:
        return None

    data = response.json().get("data").get("children")
    for item in data:
        title = item.get("data").get("title")
        print(title)
