# === FILE: task_commands.py ===
from datetime import datetime
from task_utils import get_next_id, find_task
from task_file import load_tasks, save_tasks

# Add task

def add_task(description):
    tasks = load_tasks()
    task_id = get_next_id(tasks)
    now = datetime.now().isoformat()
    task = {
        'id': task_id,
        'description': description,
        'status': 'todo',
        'createdAt': now,
        'updatedAt': now
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

# Update task

def update_task(task_id, new_description):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if task:
        task['description'] = new_description
        task['updatedAt'] = datetime.now().isoformat()
        save_tasks(tasks)
        print("Task updated successfully")
    else:
        print("Task not found")

# Delete task

def delete_task(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task['id'] != task_id]
    if len(new_tasks) != len(tasks):
        save_tasks(new_tasks)
        print("Task deleted successfully")
    else:
        print("Task not found")

# Change status

def mark_status(task_id, status):
    tasks = load_tasks()
    task = find_task(tasks, task_id)
    if task:
        task['status'] = status
        task['updatedAt'] = datetime.now().isoformat()
        save_tasks(tasks)
        print(f"Task marked as {status}")
    else:
        print("Task not found")

# List tasks

def list_tasks(filter_status=None):
    tasks = load_tasks()
    if filter_status:
        tasks = [task for task in tasks if task['status'] == filter_status]
    if tasks:
        for task in tasks:
            print(f"ID: {task['id']}, Desc: {task['description']}, Status: {task['status']}, Created: {task['createdAt']}, Updated: {task['updatedAt']}")
    else:
        print("No tasks found")