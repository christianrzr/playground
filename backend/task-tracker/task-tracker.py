import sys
import json
from pathlib import Path
from datetime import datetime

TASK_FILE = Path("tasks.json")

def get_time():
    return datetime.now().astimezone().isoformat(timespec="seconds")

def load_tasks():
    if not TASK_FILE.exists():
        save_tasks([])
        return []

    try:
        with TASK_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            raise ValueError("task data must be a json list broski")

        return tasks

    except (json.JSONDecodeError, OSError, ValueError) as error:
        print(f"error loading tasks {error}")
        sys.exit(1)

def save_tasks(tasks):
    with TASK_FILE.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

def find_tasks(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return None

def add_tasks(tasks, description):
    if not description.strip():
        print("desc can't be empty.")
        return

    task_id = max((task["id"] for task in tasks), default=0) + 1

    now = get_time()

    task = {
        "id": task_id,
        "description": description.strip(),
        "status": "todo",
        "createdAt": now,
        "updatedAt": now
    }

    tasks.append(task)
    save_tasks(tasks)

    print(f"task added successfully")

def update_tasks(tasks, task_id, description):
    task = find_tasks(tasks, task_id)

    if not None:
        print(f"error task id {task_id} not found.")
        return

    if not description.strip():
        print("error description cannot be empty.")
        return
    
    task["description"] = description.strip()
    task["updatedAt"] = get_time()

    save_tasks(tasks)
    print("updated successfully")

def delete_tasks(tasks,task_id):
    task = find_tasks(tasks, task_id)

    if not tasks:
        print("not found. try to use list")
        return

    tasks.remove(task)
    save_tasks(tasks)

    print("task deleted successfully.")

def mark_tasks(tasks, task_id, status):
    task = find_tasks(tasks,task_id)

    if not task:
        print(f"task id:{task_id} can't be found")
        return

    task["status"] = status
    task["updatedAt"] = get_time()

    save_tasks(tasks)
    print(f"task marked as {status}")

def list_tasks(tasks, status=None):
    filtered_tasks = [
        task for task in tasks
        if status is None or task["status"] == status
    ]

    if not filtered_tasks:
        print("no task found.")
        return

    for task in filtered_tasks:
        print(
            f'[{task["id"]}] {task["description"]}'
            f'| {task["status"]} '
            f'| Updated: {task["updatedAt"]}'
        )

def main():
    tasks = load_tasks()
    args = sys.argv[1:]

    if not args:
        print("usage: python task-tracker.py <command here> <arguments/description>")
        return

    command = args[0]

    try:
        if command == "add" and len(args) == 2:
            add_tasks(tasks, args[1])

        elif command == "update" and len(args) == 3:
            task_id = int(args[1])
            update_tasks(tasks, task_id, args[2])

        elif command == "delete" and len(args) == 2:
            task_id = int(args[1])
            delete_tasks(tasks, task_id)

        elif command in ("mark-in-progress", "mark-done") and len(args) == 2:
            task_id = int(args[1])
            status = (
                "in-progress"
                if command == "mark-in-progress"
                else "done"
            )

            mark_tasks(tasks, task_id, status)

        elif command == "list" and len(args) in (1,2):
            status = args[1] if len(args) == 2 else None

            if status not in (None, "todo", "done", "in-progress"):
                print("error invalid status.")
                return

            list_tasks(tasks, status)
        else:
            print("invalid command or arguments.")
            print("run 'python task-tracker.py' and read readme.md to see the usage.")

    except ValueError:
        print("error task id must be a valid integer bro")

    except OSError as error:
        print(f"file error {error}")

if __name__ == "__main__":
    main()
