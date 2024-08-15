#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API
and returns a list containing the titles of all hot articles for a given
subreddit. If no results are found for the given subreddit, the function
returns None.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively get the titles of all hot posts for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.
        hot_list (list): A list to store the titles of hot posts.
        after (str): The "after" parameter for pagination.

    Returns:
        list: A list of titles of hot posts, or None if the subreddit
              is invalid or there are no results.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-custom-user-agent'}
    params = {'after': after, 'limit': 100}  # Limit to 100 posts per request

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            posts = data.get('data', {}).get('children', [])
            if not posts and not hot_list:
                return None  # If no posts and hot_list is still empty, return None

            hot_list.extend([post.get('data', {}).get('title') for post in posts])

            # Check if there's more data to fetch (pagination)
            after = data.get('data', {}).get('after')
            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None
    except requests.RequestException:
        return None


if __name__ == '__main__':

    titles = recurse('python')
    if titles:
        print(f"Number of titles: {len(titles)}")
        for title in titles:
            print(title)
    else:
        print("No results found.")
