#!/usr/bin/python3
"""a Python script that takes your GitHub credentials
(username and password)
and uses the GitHub API to display your id
"""
if __name__ == "__main__":
    import requests
    import sys

    url = "https://api.github.com/user"
    user = sys.argv[1]
    passwd = sys.argv[2]

    r = requests.get(url, auth=(user, passwd))
    try:
        r_json = r.json()
        print(r_json["id"])
    except Exception:
        print("None")
