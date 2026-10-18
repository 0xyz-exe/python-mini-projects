"""CLI Task Manager - Core functionality."""
import json
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Optional
from dataclasses import dataclass, asdict


@dataclass
class Task:
    """Task representation."""
    id: int
    title: str
    priority: str = "medium"
    status: str = "pending"
    deadline: Optional[str] = None
    created_at: str = ""
    
    def __post_init__(self):
        if not self.created_at:
            self.created_at = datetime.now().isoformat()


class TaskManager:
    """Manage tasks with JSON persistence."""
    
    def __init__(self, storage_path: Path):
        self.storage_path = storage_path
        self.tasks: List[Task] = []
        self.load()
    
    def load(self):
        """Load tasks from JSON."""
        if self.storage_path.exists():
            with open(self.storage_path) as f:
                data = json.load(f)
                self.tasks = [Task(**t) for t in data]
    
    def save(self):
        """Save tasks to JSON."""
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.storage_path, 'w') as f:
            json.dump([asdict(t) for t in self.tasks], f, indent=2)
    
    def add(self, title: str, priority: str = "medium", deadline: Optional[str] = None) -> Task:
        """Add new task."""
        if not title.strip():
            raise ValueError("Title cannot be empty")
        if priority not in ["low", "medium", "high"]:
            raise ValueError("Priority must be low, medium, or high")
        
        task_id = max([t.id for t in self.tasks], default=0) + 1
        task = Task(id=task_id, title=title, priority=priority, deadline=deadline)
        self.tasks.append(task)
        self.save()
        return task
    
    def edit(self, task_id: int, title: Optional[str] = None, 
             priority: Optional[str] = None, deadline: Optional[str] = None) -> Task:
        """Edit existing task."""
        task = self._find_task(task_id)
        if title is not None:
            if not title.strip():
                raise ValueError("Title cannot be empty")
            task.title = title
        if priority is not None:
            if priority not in ["low", "medium", "high"]:
                raise ValueError("Priority must be low, medium, or high")
            task.priority = priority
        if deadline is not None:
            task.deadline = deadline
        self.save()
        return task
    
    def delete(self, task_id: int):
        """Delete task."""
        task = self._find_task(task_id)
        self.tasks.remove(task)
        self.save()
    
    def complete(self, task_id: int) -> Task:
        """Mark task as complete."""
        task = self._find_task(task_id)
        task.status = "completed"
        self.save()
        return task
    
    def list_tasks(self, status: Optional[str] = None, 
                   priority: Optional[str] = None) -> List[Task]:
        """List tasks with optional filters."""
        tasks = self.tasks
        if status:
            tasks = [t for t in tasks if t.status == status]
        if priority:
            tasks = [t for t in tasks if t.priority == priority]
        return sorted(tasks, key=lambda t: t.id)
    
    def _find_task(self, task_id: int) -> Task:
        """Find task by ID or raise."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        raise ValueError(f"Task {task_id} not found")
