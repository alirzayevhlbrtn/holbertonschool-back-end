#!/usr/bin/python3
"""
task 0
"""
import requests
import sys


def get_todo_rest_api(id):
    """request function"""
    url = "https://jsonplaceholder.typicode.com"
    user_url = f"{url}/users/{id}"

    response = requests.get(user_url)
    user_data = response.json()

    name = user_data['name']

    todo_url = f"{url}/todos?userId={id}"

    response = requests.get(todo_url)
    todos_data = response.json()

    total_tasks = len(todos_data)
    completed = sum(1 for todo in todos_data if todo['completed'])

    print(f"Employee {name} is done with tasks({completed}/{total_tasks}):")
    for todo in todos_data:
        if todo.get('completed', False):
            print("\t" + " " + f"{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) == 2:
        id = int(sys.argv[1])
        get_todo_rest_api(id)
