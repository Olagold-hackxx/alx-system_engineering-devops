#!/usr/bin/python3
""" A function that queries the Reddit API and returns
the top ten hot articles of a given subreddit"""


def top_ten(subreddit):
    """Query api"""
    import requests

    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "api_advanved_task_0"

    headers = {'User-Agent': user_agent}
    res = requests.get(url, headers=headers, params={"limit": 10})

    try:
        res = res.json()
        data = res['data']['children']
        if not data:
            print(None)
        for sub_red in data:
            print(sub_red.get('data').get('title'))
    except Exception:
        return None
