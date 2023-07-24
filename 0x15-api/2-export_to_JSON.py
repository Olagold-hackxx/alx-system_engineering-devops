#!/usr/bin/python3
"""REST api"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user = 'https://jsonplaceholder.typicode.com/users'
    todo = 'https://jsonplaceholder.typicode.com/todos'

    user_req = requests.get(user, params={id: argv[1]})

    user_res = user_req.json()
    for user in user_res:
        if int(argv[1]) == user.get("id"):
            filename = argv[1] + '.json'
            todo_req = requests.get(todo, params={'userId': argv[1]})
            todo_res = todo_req.json()
            user_details = {}
            tasks = []
            user_id = user.get("id")
            for todos in todo_res:
                details = {}

                details["task"] = todos.get('title')
                details["completed"] = todos.get('completed')
                details["name"] = user.get('username')
                tasks.append(details)
            user_details[user_id] = tasks
            with open(filename, mode='a', encoding='utf8') as userJson:
                json.dump(user_details, userJson)
