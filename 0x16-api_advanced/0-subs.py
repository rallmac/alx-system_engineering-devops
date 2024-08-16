#!/usr/bin/python3
"""
This function queries the Reddit API and returns the number
of subscribers for a given subreddit.
"""

import requests


def number_of_subscribers(subreddit):
    """Return the number of subscribers for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-custom-user-agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            return data.get('data', {}).get('subscribers', 0)
        elif response.status_code == 302:
            # Handles redirection, which indicates an invalid subreddit
            return 0
        else:
            return 0
    except requests.RequestException:
        return 0


if __name__ == '__main__':
    subreddit = input("Enter the name of the subreddit: ")
    subscribers = number_of_subscribers(subreddit)
    print(f"Number of subscribers: {subscribers}")
