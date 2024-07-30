#!/usr/bin/python3
"""
A script that fetches data from an API
"""

import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"

    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    task = requests.get(url + "todos", data={"userId": (sys.argv[1])}).json()
    complete = []
    for t in task:
        if t.get('completed') is True:
            complete.append(t.get('title'))

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(complete), len(task)))
    for c in complete:
        print("\t {}".format(c))
