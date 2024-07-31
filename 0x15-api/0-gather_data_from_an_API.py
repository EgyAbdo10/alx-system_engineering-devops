#!/usr/bin/python3
"""get data from https://jsonplaceholder.typicode.com/"""


import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]
    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    emp_response = requests.get(emp_url)
    # print(response.text)
    emp_name = emp_response.json()["name"]
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    tasks_response = requests.get(tasks_url)
    tasks_list = tasks_response.json()
    total_tasks_number = len(tasks_list)
    tasks_completed_number = 0
    tasks_completed_titles = ""
    for task in tasks_list:
        if task["completed"]:
            tasks_completed_number += 1
            tasks_completed_titles += f"     {task['title']}\n"
    print(f"Employee {emp_name} is done with tasks"
          + f"({tasks_completed_number}/{total_tasks_number}):")
    print(tasks_completed_titles, end="")
