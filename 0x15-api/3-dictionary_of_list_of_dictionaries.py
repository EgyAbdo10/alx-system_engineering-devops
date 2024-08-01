#!/usr/bin/python3
"""get all employees data from https://jsonplaceholder.typicode.com/
and export it as a json file
"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    emp_id = 1
    emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
    emp_response = requests.get(emp_url)
    emp_name = emp_response.json()["username"]
    emp_dict_list = []
    while emp_response.ok:
        tasks_url = ("https://jsonplaceholder" +
                     f".typicode.com/todos?userId={emp_id}")
        tasks_response = requests.get(tasks_url)
        tasks_list = tasks_response.json()
        tasks_list_of_dict = []
        emp_name = emp_response.json()["username"]
        for task in tasks_list:
            tasks_list_of_dict.append({"username": emp_name,
                                       "task": task["title"],
                                       "completed": task["completed"]})
        emp_dict_list.append({str(emp_id): tasks_list_of_dict})
        emp_id += 1
        emp_url = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
        emp_response = requests.get(emp_url)
    with open('todo_all_employees.json', "w") as f:
        json.dump(emp_dict_list, f)
