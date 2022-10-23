#!/usr/bin/python3
"""script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a
parameter,and displays
the body of the response (decoded in utf-8)
"""

if __name__ == "__main__":
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    import sys

    data = {'email': sys.argv[2]}
    req = Request(sys.argv[1], urlencode(data).encode())
    with urlopen(req) as response:
        response = urlopen(req).read().decode('utf-8')
        print(response)
