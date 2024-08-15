#!/usr/bin/python3
"""get the numebr of active subscribers of a subreddit"""


import requests


def number_of_subscribers(subreddit):
    """send a request to a reddit api"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, allow_redirects=False)
    if response.status_code >= 400:
        return 0

    data_dict = response.json()
    return data_dict["data"]["subscribers"]
