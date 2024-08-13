#!/usr/bin/python3
'''
A function that queries REDDIT API and returns the number of subreddits
'''

import requests

headers = {'User-Agent': 'python:subscribers.counter:v1:0:0 (by semkufu)'}


def number_of_subscribers(subreddit):
    """ set header to avoid too many requests errors """
    api_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    result = requests.get(api_url, headers=headers, allow_redirects=False)

    # check if subredit is valid
    if result.status_code == 200:
        data = result.json().get('data', {})
        if not data:
            return 0
        return data.get('subscribers', 0)
    else:
        return 0
