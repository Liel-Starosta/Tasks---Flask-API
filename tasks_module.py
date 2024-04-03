import json

TASKS_DB = "/home/lielst/Desktop/task_api/tasks_db.json"

def load_tasks():
    with open(TASKS_DB, "r") as file:
        data = json.load(file)
    return data

def get_task_by_id(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None

def delete_task(tasks, task_id):
    tasks[:] = [task for task in tasks if task['id'] != task_id]

def create_task(data, all_tasks):
    task_id = max([task['id'] for task in all_tasks]) + 1
    new_task = {
        "title": data['title'],
        "description": data['description'],
        "id": task_id
    }
    return new_task

def update_task(task, data):
    task['title'] = data.get('title', task['title'])
    task['description'] = data.get('description', task['description'])
    return task

def save_tasks(tasks):
    with open(TASKS_DB, "w") as file:
        json.dump(tasks, file, indent=4)
