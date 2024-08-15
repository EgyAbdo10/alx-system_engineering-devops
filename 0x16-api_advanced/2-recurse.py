#!/usr/bin/python3
"""get the titles of subreddit recursively"""


import requests


def recurse(subreddit, hot_list=[], limit=1):
    """return the first 10 hot posts for a subreddit"""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {"limit": limit}
    response = requests.get(url=url, allow_redirects=False,
                            headers=headers, params=params)
    if response != 200:
        return None
    data = response.json().get("data").get("children")
    title = data[-1].get("data").get("title")

    hot_list.append(title)
    

