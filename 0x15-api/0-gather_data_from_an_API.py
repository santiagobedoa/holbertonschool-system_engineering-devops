#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import requests
from sys import argv


def get_info():
    # ORIGINAL ANSWER
    # url_employee = "https://jsonplaceholder.typicode.com/users/"
    # employee_info = (requests.get("{}{}".format(
    # url_employee, argv[1]))).json()
    # url_tasks = "https://jsonplaceholder.typicode.com/todos?userId="
    # tasks_info = (requests.get("{}{}".format(url_tasks, argv[1]))).json()
    # total_tasks = 0
    # completed_tasks = list()
    # for task in tasks_info:
    #     total_tasks += 1
    #     if task["completed"] is True:
    #         completed_tasks.append(task)
    # print("Employee {} is done with tasks ({}/{}):".format(
    #     employee_info["name"],
    #     len(completed_tasks),
    #     total_tasks,
    # ))
    # for task in completed_tasks:
    #     print("\t {}".format(task["title"]))
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    completed_tasks = []
    for task in todo:
        if task.get('completed') is True:
            completed_tasks.append(task.get('title'))
    print("Employee {} is done with tasks({}/{}):".
          format(user.get('name'), len(completed_tasks), len(todo)))
    print("\n".join("\t {}".format(task) for task in completed_tasks))


if __name__ == "__main__":
    get_info()
