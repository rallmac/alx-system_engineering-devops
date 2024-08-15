#!/usr/bin/python3
"""This function queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """Prints the titles of the first 10 hot posts for a given subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'my-custom-user-agent'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if posts:
                for post in posts:
                    print(post.get('data', {}).get('title'))
            else:
                print(None)
        else:
            print(None)
    except requests.RequestException:
        print(None)


if __name__ == '__main__':
    subreddit = input("Enter the name of the subreddit: ")
    top_ten(subreddit)
