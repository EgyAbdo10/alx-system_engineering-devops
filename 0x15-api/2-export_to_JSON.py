#!/usr/bin/python3
"""get data from https://jsonplaceholder.typicode.com/
and export it as a json file
"""
import json
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
    tasks_list_of_dict = []
    for task in tasks_list:
        tasks_list_of_dict.append({"task": task["title"],
                                   "completed": task["completed"],
                                   "username": emp_name})
    json_dict = {str(emp_id): tasks_list_of_dict}
    with open(f'{emp_id}.json', "w") as f:
        json.dump(json_dict, f)
