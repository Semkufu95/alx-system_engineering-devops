#!/usr/bin/python3
"""
A script to gather data from an API
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url +"users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", data={"userId": sys.argv[1]}).json()

    complete = [k.get("title") for k in todos if k.get('completed') is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(complete), len(todos)))
    [print("\t {}".format(i)) for i in complete]
