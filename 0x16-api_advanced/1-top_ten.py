#!/usr/bin/python3
"""get the titles of subreddit"""


import requests


def top_ten(subreddit):
    """return the first 10 hot posts for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by me)"
    }
    params = {"limit": 9}
    response = requests.get(url=url, allow_redirects=False,
                            headers=headers, params=params)
    if response.status_code != 200:
        print("None")
        return

    data = response.json().get("data").get("children")
    i = 0
    for item in data:
        title = item.get("data").get("title")
        print(title)
        i += 1
    return
