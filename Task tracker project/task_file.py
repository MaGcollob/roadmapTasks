import os
import json

# ✅ Safe path for tasks.json
TASK_FILE = os.path.join(os.path.dirname(__file__), 'tasks.json')

# ✅ Create file if not exist
def initialize_file():
    if not os.path.exists(TASK_FILE):
        with open(TASK_FILE, 'w') as f:
            json.dump([], f)

# ✅ Load all tasks from file
def load_tasks():
    with open(TASK_FILE, 'r') as f:
        return json.load(f)

# ✅ Save updated tasks to file
def save_tasks(tasks):
    with open(TASK_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)
