#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import requests
from sys import argv
import json


def info_to_json():
    url_employee = "https://jsonplaceholder.typicode.com/users/"
    employee_info = (requests.get("{}{}".format(url_employee, argv[1]))).json()
    url_tasks = "https://jsonplaceholder.typicode.com/todos?userId="
    tasks = (requests.get("{}{}".format(url_tasks, argv[1]))).json()
    json_obj = {}
    list_of_task = []
    for task in tasks:
        task_dict = {}
        task_dict["task"] = task["title"]
        task_dict["completed"] = task["completed"]
        task_dict["username"] = employee_info["name"]
        list_of_task.append(task_dict)
    json_obj[str(argv[1])] = list_of_task
    with open("{}.json".format(argv[1]), 'w') as f:
        json.dump(json_obj, f)


if __name__ == "__main__":
    info_to_json()
