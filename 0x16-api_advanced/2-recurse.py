#!/usr/bin/python3
""" A function that queries the Reddit API and returns
the all hot articles of a given subreddit"""

import requests


def query_recursive(subred_data, counter, hot_list):
    """Query all hot article in a each page recursively"""

    try:
        title = subred_data[counter].get('data').get('title')
    except Exception:
        return hot_list
    if type(title) == str:
        hot_list.append(title)
        counter = counter + 1
        return query_recursive(subred_data, counter, hot_list)


def recurse(subreddit, hot_list=[], after=None, count=0):
    """Query all hot articles of a given subreddit"""
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "api_advanved_task_0"

    headers = {'User-Agent': user_agent}
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    res = requests.get(url, headers=headers, params=params)

    try:
        if res.status_code != 200:
            return None
        res = res.json()
        subreddit_data = res.get('data').get('children')
        if not subreddit_data and len(hot_list) < 1:
            return None
        counter = 0
        hot_list = query_recursive(subreddit_data, counter, hot_list)
        after = res['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list=hot_list, after=after)
        else:
            return hot_list

    except Exception:
        return None
