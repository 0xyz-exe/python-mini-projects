#!/usr/bin/env python3
"""CLI Task Manager - Command line interface."""
import argparse
from pathlib import Path
from task_manager import TaskManager


def main():
    parser = argparse.ArgumentParser(description="CLI Task Manager")
    parser.add_argument("--storage", default="tasks.json", help="Storage file path")
    
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # Add command
    add_parser = subparsers.add_parser("add", help="Add new task")
    add_parser.add_argument("title", help="Task title")
    add_parser.add_argument("-p", "--priority", choices=["low", "medium", "high"], 
                           default="medium", help="Task priority")
    add_parser.add_argument("-d", "--deadline", help="Task deadline")
    
    # Edit command
    edit_parser = subparsers.add_parser("edit", help="Edit existing task")
    edit_parser.add_argument("id", type=int, help="Task ID")
    edit_parser.add_argument("-t", "--title", help="New title")
    edit_parser.add_argument("-p", "--priority", choices=["low", "medium", "high"], 
                            help="New priority")
    edit_parser.add_argument("-d", "--deadline", help="New deadline")
    
    # Delete command
    delete_parser = subparsers.add_parser("delete", help="Delete task")
    delete_parser.add_argument("id", type=int, help="Task ID")
    
    # Complete command
    complete_parser = subparsers.add_parser("complete", help="Mark task complete")
    complete_parser.add_argument("id", type=int, help="Task ID")
    
    # List command
    list_parser = subparsers.add_parser("list", help="List tasks")
    list_parser.add_argument("-s", "--status", choices=["pending", "completed"], 
                            help="Filter by status")
    list_parser.add_argument("-p", "--priority", choices=["low", "medium", "high"], 
                            help="Filter by priority")
    
    args = parser.parse_args()
    
    try:
        tm = TaskManager(Path(args.storage))
        
        if args.command == "add":
            task = tm.add(args.title, args.priority, args.deadline)
            print(f"✓ Added task #{task.id}: {task.title}")
        
        elif args.command == "edit":
            task = tm.edit(args.id, args.title, args.priority, args.deadline)
            print(f"✓ Updated task #{task.id}")
        
        elif args.command == "delete":
            tm.delete(args.id)
            print(f"✓ Deleted task #{args.id}")
        
        elif args.command == "complete":
            task = tm.complete(args.id)
            print(f"✓ Completed task #{task.id}: {task.title}")
        
        elif args.command == "list":
            tasks = tm.list_tasks(args.status, args.priority)
            if not tasks:
                print("No tasks found")
            else:
                for task in tasks:
                    status_icon = "✓" if task.status == "completed" else "○"
                    deadline = f" (due: {task.deadline})" if task.deadline else ""
                    print(f"{status_icon} #{task.id} [{task.priority}] {task.title}{deadline}")
    
    except Exception as e:
        print(f"Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
