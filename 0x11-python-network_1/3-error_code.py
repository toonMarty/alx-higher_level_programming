#!/usr/bin/python3
"""a Python script that takes in a URL, sends a request to the URL and
displays the body of the response
(decoded in utf-8)"""
if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    import sys
    import urllib

    req = Request(sys.argv[1])
    try:
        with urlopen(req) as response:
            response = urlopen(req).read().decode('utf-8')
            print(response)
    except urllib.error.HTTPError as e:
        print('Error code:', e.code)
