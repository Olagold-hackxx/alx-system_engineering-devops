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
    else:
        hot_list.append(title)
        counter = counter + 1
        return query_recursive(subred_data, counter, hot_list)


def recurse(subreddit, hot_list=[], after=None):
    """Query all hot articles of a given subreddit"""
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "api_advanved_task_0"

    headers = {'User-Agent': user_agent}
    if after is not None:
        url = url + "?after={}".format(after)
    res = requests.get(url, headers=headers)

    try:
        res = res.json()
        subreddit_data = res['data']['children']
        if not subreddit_data:
            return None
        counter = 0
        hot_list.append(query_recursive(subreddit_data, counter, hot_list))
        after = res['data']['after']
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list

    except Exception:
        return None


def count_words(subreddit, word_list, counter=0, result=[]):
    """parses the title of all hot articles, and prints a sorted count of given
    keywords (case-insensitive, delimited by spaces"""
    hotlist = recurse(subreddit)
    word_list_lower = [x.lower() for x in word_list]
    keyword = word_list_lower[counter]
    if not keyword:
        return result
    else:
        result.append(search_keyword(keyword, hotlist, occurence=0, count=0))
        return count_words(subreddit, word_list_lower, counter=counter + 1, result=result)


def search_keyword(keyword, hotlist, occurence, count):
    if not hotlist[count]:
        return {keyword: occurence}
    else:
        if keyword in hotlist[count].lower():
            occurence = occurence + hotlist[count].lower().count(keyword)
        return search_keyword(keyword, hotlist, occurence=occurence, count=count + 1)
