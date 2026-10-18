# CLI Task Manager

Command-line task manager with priorities, deadlines, and filters.

## Features

- Add, edit, delete tasks
- Set priorities (low/medium/high)
- Set deadlines
- Mark tasks complete
- Filter by status and priority
- JSON persistence

## Usage

```bash
cd projects/01-cli-task-manager/src

# Add task
python cli.py add "Buy groceries" -p high -d 2026-10-20

# List all tasks
python cli.py list

# List pending high-priority tasks
python cli.py list -s pending -p high

# Complete task
python cli.py complete 1

# Edit task
python cli.py edit 1 -t "Buy milk" -p medium

# Delete task
python cli.py delete 1
```

## Testing

```bash
cd projects/01-cli-task-manager
python tests/test_task_manager.py
```

## Dependencies

Python 3.11+ (stdlib only)
