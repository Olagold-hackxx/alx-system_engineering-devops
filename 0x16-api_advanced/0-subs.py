#!/usr/bin/python3
""" A function that queries the Reddit API and returns
the number of subscribers
(not active users, total subscribers) for a given subreddit."""


def number_of_subscribers(subreddit):
    """Query api"""
    import requests

    url = "https://reddit.com/r/{}/about.json".format(subreddit)
    user_agent = "api_advanved_task_0"
    headers = {'User-Agent': user_agent, 'Accept': 'application/json'}

    req = requests.get(url, headers=headers)

    try:
        res = req.json()
        data = res.get('data')
        subreddit_subscribers = data['subscribers']
        return subreddit_subscribers
    except Exception:
        return 0
