from datetime import datetime
from task_file import load_tasks, save_tasks

# Get next ID

def get_next_id(tasks):
    if not tasks:
        return 1
    return max(task['id'] for task in tasks) + 1

# Find task

def find_task(tasks, task_id):
    for task in tasks:
        if task['id'] == task_id:
            return task
    return None