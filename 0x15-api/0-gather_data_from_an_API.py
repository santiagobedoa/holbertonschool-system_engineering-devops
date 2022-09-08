#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import requests
from sys import argv


def get_info():
    url_employee = "https://jsonplaceholder.typicode.com/users/"
    employee_info = (requests.get("{}{}".format(url_employee, argv[1]))).json()
    url_tasks = "https://jsonplaceholder.typicode.com/todos?userId="
    tasks_info = (requests.get("{}{}".format(url_tasks, argv[1]))).json()
    total_tasks = 0
    completed_tasks = list()
    for task in tasks_info:
        total_tasks += 1
        if task["completed"] is True:
            completed_tasks.append(task)
    print("Employee {} is done with tasks ({}/{}):".format(
        employee_info["name"],
        len(completed_tasks),
        total_tasks,
    ))
    for task in completed_tasks:
        print("\t {}".format(task["title"]))


if __name__ == "__main__":
    get_info()
