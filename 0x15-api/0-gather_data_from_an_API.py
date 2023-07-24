#!/usr/bin/python3
"""REST api"""
import requests
from sys import argv


if __name__ == '__main__':
    user = 'https://jsonplaceholder.typicode.com/users'
    todo = 'https://jsonplaceholder.typicode.com/todos'

    user_req = requests.get(user, params={id: argv[1]})

    user_res = user_req.json()
    for user in user_res:
        if int(argv[1]) == user.get("id"):
            todo_req = requests.get(todo, params={'userId': argv[1]})
            todo_res = todo_req.json()
            completed_task = 0
            tasks = 0
            tasks_titles = []
            for todos in todo_res:
                tasks = tasks + 1
                if todos.get('completed') is True:
                    tasks_titles.append(todos.get('title'))
                    completed_task = completed_task + 1
            print('Employee {} is done with tasks({}/{}):'.format(
                user.get('name'), completed_task, tasks))
            for title in tasks_titles:
                print('\t {}'.format(title))
