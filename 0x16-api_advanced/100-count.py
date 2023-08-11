#!/usr/bin/python3
""" A function that queries the Reddit API and returns
the all hot articles of a given subreddit"""

import requests


def count_words(subreddit, word_list, counter=0, result=[]):
    recurse = __import__('2-recurse').recurse
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
    try:
        hotlist[count]
    except Exception:
        return {keyword: occurence}
    else:
        if keyword in hotlist[count].lower():
            occurence = occurence + hotlist[count].lower().count(keyword)
        return search_keyword(keyword, hotlist, occurence=occurence, count=count + 1)
