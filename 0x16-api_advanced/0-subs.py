#!/usr/bin/python3
"""
Script that queries subscribers on a given Reddit subreddit.
"""
import json
import urllib.request


def number_of_subscribers(subreddit):
    """Return the total number of subscribers on a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as response:
            if response.status == 200:
                print(response.headers)
                data = json.loads(response.read().decode())
                subscribers = data['data']['subscribers']
                return subscribers
            else:
                return 0
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code}, Reason: {e.reason}")
        return 0
    except urllib.error.URLError as e:
        print(f"URL Error: {e.reason}")
        return 0
