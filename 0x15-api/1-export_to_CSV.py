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
            filename =  argv[1] + '.csv'
            for todos in todo_res:
                user_id = user.get('id')
                username = user.get('username')
                todo_status = todos.get('completed')
                todo_title =  todos.get('title')
                with open(filename, mode='a', encoding='utf8') as user_details:
                    user_details.write('"{}","{}","{}","{}"\n'.format(user_id, username, todo_status, todo_title))
