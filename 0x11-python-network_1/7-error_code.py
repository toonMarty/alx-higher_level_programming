#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the
   URL and displays the body of the response
"""
if __name__ == "__main__":
    from requests.exceptions import HTTPError
    import sys
    import requests

    try:
        r = requests.get(sys.argv[1])
        r.raise_for_status()
        print(r.text)
    except HTTPError as e:
        print(f'Error code: {e.response.status_code}')
