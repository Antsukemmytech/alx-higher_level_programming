#!/usr/bin/python3
"""Fetches https://github.com/Antsukemmytech/alx-higher_level_programming."""
import urllib.request

if __name__ == "__main__":
    request = urllib.request.Request("https://github.com/Antsukemmytech/alx-higher_level_programming")
    with urllib.request.urlopen(request) as response:
        x_request_id = response.headers.get('X-Request-Id')
        print("X-Request-Id:", x_request_id)

