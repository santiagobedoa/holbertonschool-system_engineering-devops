#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import requests
import json


def info_to_json():
    url_employee = "https://jsonplaceholder.typicode.com/users/"
    all_employees = (requests.get(url_employee)).json()
    url_tasks = "https://jsonplaceholder.typicode.com/todos?userId="
    json_obj = {}
    for employee in all_employees:
        employee_info = (requests.get("{}{}".format(
            url_employee,
            str(employee["id"])
        ))).json()
        tasks = (requests.get("{}{}".format(
            url_tasks,
            str(employee["id"])
        ))).json()
        list_of_task = []
        for task in tasks:
            task_dict = {}
            task_dict["username"] = employee_info["name"]
            task_dict["task"] = task["title"]
            task_dict["completed"] = task["completed"]
            list_of_task.append(task_dict)
        json_obj[str(employee["id"])] = list_of_task
    with open("todo_all_employees.json", 'w') as f:
        json.dump(json_obj, f)


if __name__ == "__main__":
    info_to_json()
