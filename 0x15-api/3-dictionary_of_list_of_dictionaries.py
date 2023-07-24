#!/usr/bin/python3
"""REST api"""
import json
import requests
from sys import argv


if __name__ == '__main__':
    user = 'https://jsonplaceholder.typicode.com/users'
    todo = 'https://jsonplaceholder.typicode.com/todos'

    user_req = requests.get(user)

    user_res = user_req.json()
    user_details = {}
    for user in user_res:
        todo_req = requests.get(todo, params={'userId': user.get('id')})
        todo_res = todo_req.json()
        tasks = []
        user_id = user.get("id")
        for todos in todo_res:
            details = {}
            details["task"] = todos.get('title')
            details["completed"] = todos.get('completed')
            details["username"] = user.get('username')
            tasks.append(details)
        user_details[user_id] = tasks
    with open('todo_all_employees.json',
              mode='w', encoding='utf8') as userJson:
        json.dump(user_details, userJson)
