#!/usr/bin/python3
"""a Python script that takes 2 arguments in order to solve
this challenge
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/repos/{}/{}/commits".\
        format(sys.argv[2], sys.argv[1])

    r = requests.get(url)
    commits = r.json()

    try:
        for i in range(10):
            print("{}: {}".format(commits[i].get("sha"), commits[i].
                                  get("commit").get("author").get("name")))
    except IndexError:
        pass
