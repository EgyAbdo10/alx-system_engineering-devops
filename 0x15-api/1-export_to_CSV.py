#!/usr/bin/python3
"""get data from https://jsonplaceholder.typicode.com/
and export it as a csv file
"""
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = argv[1]
    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    emp_response = requests.get(emp_url)
    # print(response.text)
    emp_name = emp_response.json()["username"]
    tasks_url = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"
    tasks_response = requests.get(tasks_url)
    tasks_list = tasks_response.json()
    with open(f'{emp_id}.csv', "w") as f:
        for task in tasks_list:
            f.write(f'"{emp_id}","{emp_name}",' +
                    '"{task["completed"]}","{task["title"]}"\n')
