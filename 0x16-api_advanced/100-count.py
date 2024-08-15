#!/usr/bin/python3
"""
This module contains a recursive function that queries the Reddit API,
parses the titles of all hot articles, and prints a sorted count of given
keywords (case-insensitive).
"""

import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """
    Recursively count the occurrences of keywords in hot article titles
    for a given subreddit.

    Args:
        subreddit (str): The subreddit to query.
        word_list (list): A list of keywords to count.
        word_count (dict): A dictionary to store the count of keywords.
        after (str): The "after" parameter for pagination.

    Returns:
        None: The function prints the results.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'my-custom-user-agent'}
    params = {'after': after, 'limit': 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code != 200:
            return

        data = response.json()
        posts = data.get('data', {}).get('children', [])

        if not posts:
            return

        # Convert word_list to lowercase for case-insensitivity
        word_list = [word.lower() for word in word_list]

        # Count occurrences of each keyword in the titles
        for post in posts:
            title = post.get('data', {}).get('title', '').lower()
            for word in word_list:
                # Check for exact matches only (not substrings)
                title_words = title.split()
                word_count[word] = word_count.get(word, 0) + title_words.count(word)

        # Check if there's more data to fetch (pagination)
        after = data.get('data', {}).get('after')
        if after:
            return count_words(subreddit, word_list, word_count, after)
        
        # Sort and print the results after recursion is complete
        if word_count:
            sorted_word_count = sorted(word_count.items(),
                                       key=lambda item: (-item[1], item[0]))
            for word, count in sorted_word_count:
                if count > 0:
                    print(f"{word}: {count}")

    except requests.RequestException:
        return


if __name__ == '__main__':

    subreddit = input("Enter the name of the subreddit: ")
    word_list = input("Enter the keywords (separated by spaces): ").split()
    count_words(subreddit, word_list)
