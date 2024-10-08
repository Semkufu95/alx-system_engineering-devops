#!/usr/bin/python3
"""Module that consumes the Reddit API and returns a list containing the
titles of all hot articles for a given subreddit."""
import requests


def recurse(subreddit, hot_list=[], n=0, after=None):
    """
    queries the Reddit API and returns a list containing the titles of
    all hot articles for a given subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    headers = {'user-agent': 'custom'}
    result = requests.get(url, headers=headers, allow_redirects=False)
    if result.status_code == 200:
        result = result.json()
        for post in result.get('data').get('children'):
            hot_list.append(post.get('data').get('title'))
        if result.get('data').get('after'):
            recurse(subreddit, hot_list)
        return hot_list
    else:
        return None
