#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import json
import requests
from sys import argv


def info_to_json():
    # original answer
    # url_employee = "https://jsonplaceholder.typicode.com/users/"
    # employee_info = (requests.get("{}{}".format(
    # url_employee, argv[1]))).json()
    # url_tasks = "https://jsonplaceholder.typicode.com/todos?userId="
    # tasks = (requests.get("{}{}".format(url_tasks, argv[1]))).json()
    # json_obj = {}
    # list_of_task = []
    # for task in tasks:
    #     task_dict = {}
    #     task_dict["task"] = task["title"]
    #     task_dict["completed"] = task["completed"]
    #     task_dict["username"] = employee_info["name"]
    #     list_of_task.append(task_dict)
    # json_obj[str(argv[1])] = list_of_task
    # with open("{}.json".format(argv[1]), 'w') as f:
    #     json.dump(json_obj, f)
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    username = user.get('username')
    tasks = []
    for task in todo:
        task_dict = {}
        task_dict["task"] = task.get('title')
        task_dict["completed"] = task.get('completed')
        task_dict["username"] = username
        tasks.append(task_dict)
    jsonobj = {}
    jsonobj[userId] = tasks
    with open("{}.json".format(userId), 'w') as jsonfile:
        json.dump(jsonobj, jsonfile)


if __name__ == "__main__":
    info_to_json()
