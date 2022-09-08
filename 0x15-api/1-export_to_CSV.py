#!/usr/bin/python3
"""
Uses https://jsonplaceholder.typicode.com along with an employee ID to
return information about the employee's todo list progress
"""

import requests
from sys import argv
import csv


def info_to_csv():
    url_employee = "https://jsonplaceholder.typicode.com/users/"
    employee_info = (requests.get("{}{}".format(url_employee, argv[1]))).json()
    url_tasks = "https://jsonplaceholder.typicode.com/todos?userId="
    tasks_info = (requests.get("{}{}".format(url_tasks, argv[1]))).json()

    with open("{}.csv".format(argv[1]), 'w') as f:
        csv_writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for task in tasks_info:
            csv_writer.writerow([
                int(task["userId"]),
                str(employee_info["name"]),
                str(task["completed"]),
                str(task["title"])
            ])

if __name__ == "__main__":
    info_to_csv()
