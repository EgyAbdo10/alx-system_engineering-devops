#!/usr/bin/python3
"""get the numebr of active subscribers of a subreddit"""


import requests
import sys


def number_of_subscribers(subreddit):
    """send a request to a reddit api"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    response = requests.get(url, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data_dict = response.json()
    return data_dict["data"]["active_user_count"]


print(number_of_subscribers(sys.argv[1]))
