#!/usr/bin/python3
"""Fetches https://github.com/Antsukemmytech/alx-higher_level_programming."""
import urllib.request


if __name__ == "__main__":
    request = urllib.request.Request("https://github.com/Antsukemmytech/alx-higher_level_programming")
    with urllib.request.urlopen(request) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
