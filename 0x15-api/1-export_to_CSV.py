#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import csv
import requests
from sys import argv


def info_to_csv():
    # original answer
    # url_employee = "https://jsonplaceholder.typicode.com/users/"
    # employee_info = (requests.get("{}{}".format(
    # url_employee, argv[1]))).json()
    # url_tasks = "https://jsonplaceholder.typicode.com/todos?userId="
    # tasks_info = (requests.get("{}{}".format(url_tasks, argv[1]))).json()

    # with open("{}.csv".format(argv[1]), 'w') as f:
    #     csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
    #     for task in tasks_info:
    #         csv_writer.writerow([
    #             int(task["userId"]),
    #             str(employee_info["name"]),
    #             str(task["completed"]),
    #             str(task["title"])
    #         ])
    userId = argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}".
                        format(userId), verify=False).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/todos?userId={}".
                        format(userId), verify=False).json()
    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            taskwriter.writerow([int(userId), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])


if __name__ == "__main__":
    info_to_csv()
