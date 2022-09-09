#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import json
import requests


def info_to_json():
    # original answer
    # url_employee = "https://jsonplaceholder.typicode.com/users/"
    # all_employees = (requests.get(url_employee)).json()
    # url_tasks = "https://jsonplaceholder.typicode.com/todos?userId="
    # json_obj = {}
    # for employee in all_employees:
    #     employee_info = (requests.get("{}{}".format(
    #         url_employee,
    #         str(employee["id"])
    #     ))).json()
    #     tasks = (requests.get("{}{}".format(
    #         url_tasks,
    #         str(employee["id"])
    #     ))).json()
    #     list_of_task = []
    #     for task in tasks:
    #         task_dict = {}
    #         task_dict["username"] = employee_info["name"]
    #         task_dict["task"] = task["title"]
    #         task_dict["completed"] = task["completed"]
    #         list_of_task.append(task_dict)
    #     json_obj[str(employee["id"])] = list_of_task
    # with open("todo_all_employees.json", 'w') as f:
    #     json.dump(json_obj, f)
    users = requests.get("https://jsonplaceholder.typicode.com/users",
                         verify=False).json()
    userdict = {}
    usernamedict = {}
    for user in users:
        uid = user.get("id")
        userdict[uid] = []
        usernamedict[uid] = user.get("username")
    todo = requests.get("https://jsonplaceholder.typicode.com/todos",
                        verify=False).json()
    for task in todo:
        taskdict = {}
        uid = task.get("userId")
        taskdict["task"] = task.get('title')
        taskdict["completed"] = task.get('completed')
        taskdict["username"] = usernamedict.get(uid)
        userdict.get(uid).append(taskdict)
    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(userdict, jsonfile)


if __name__ == "__main__":
    info_to_json()
