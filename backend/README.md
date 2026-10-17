# Task Tracker CLI

A simple task tracker made with Python. It lets you add, update, delete, and manage tasks through the terminal.

## Usage

```bash
py task-tracker.py add "Learn Python"
py task-tracker.py list
py task-tracker.py update 1 "Learn Python basics"
py task-tracker.py delete 1
py task-tracker.py mark-in-progress 1
py task-tracker.py mark-done 1
```

To filter tasks:

```bash
py task-tracker.py list todo
py task-tracker.py list in-progress
py task-tracker.py list done
```

Tasks are saved in `tasks.json`.

## Built With

- Python
- JSON
