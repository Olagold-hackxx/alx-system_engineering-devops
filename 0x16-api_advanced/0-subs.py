#!/usr/bin/python3


def number_of_subscribers(subreddit):
    import requests
    import json

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
