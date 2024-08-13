#!/usr/bin/python3
'''
A function that queries REDDIT API and return 10 acc.
'''
import requests


def top_ten(subreddit):
    # Set a custom User-Agent to avoid Too Many Requests errors
    headers = {'User-Agent': 'python:hot.posts.fetcher:v1.0.0 (by /u/user)'}

    # Make a GET request to the Reddit API
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid (status code 200)
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        # Print the title of each post
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
