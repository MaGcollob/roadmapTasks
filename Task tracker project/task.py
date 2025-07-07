import sys
from task_file import initialize_file
from task_commands import add_task, update_task, delete_task, mark_status, list_tasks

initialize_file()

if len(sys.argv) < 2:
    print("Usage: python task.py <command> [arguments]")
    sys.exit(1)

command = sys.argv[1]

try:
    if command == 'add':
        description = sys.argv[2]
        add_task(description)
    elif command == 'update':
        task_id = int(sys.argv[2])
        description = sys.argv[3]
        update_task(task_id, description)
    elif command == 'delete':
        task_id = int(sys.argv[2])
        delete_task(task_id)
    elif command == 'mark-in-progress':
        task_id = int(sys.argv[2])
        mark_status(task_id, 'in-progress')
    elif command == 'mark-done':
        task_id = int(sys.argv[2])
        mark_status(task_id, 'done')
    elif command == 'list':
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()
    else:
        print("Unknown command")
except IndexError:
    print("Missing argument(s). Check the command and try again.")
except ValueError:
    print("Invalid ID. Please enter a number.")
