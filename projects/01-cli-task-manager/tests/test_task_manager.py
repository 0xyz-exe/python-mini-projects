"""Tests for task manager."""
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import sys

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from task_manager import TaskManager, Task


def test_add_task():
    with TemporaryDirectory() as tmpdir:
        storage = Path(tmpdir) / "tasks.json"
        tm = TaskManager(storage)
        
        task = tm.add("Test task", "high", "2026-12-31")
        assert task.id == 1
        assert task.title == "Test task"
        assert task.priority == "high"
        assert task.deadline == "2026-12-31"
        assert task.status == "pending"


def test_add_empty_title_fails():
    with TemporaryDirectory() as tmpdir:
        tm = TaskManager(Path(tmpdir) / "tasks.json")
        try:
            tm.add("   ")
            assert False, "Should raise ValueError"
        except ValueError as e:
            assert "empty" in str(e).lower()


def test_edit_task():
    with TemporaryDirectory() as tmpdir:
        tm = TaskManager(Path(tmpdir) / "tasks.json")
        task = tm.add("Original")
        
        tm.edit(task.id, title="Updated", priority="low")
        updated = tm._find_task(task.id)
        assert updated.title == "Updated"
        assert updated.priority == "low"


def test_delete_task():
    with TemporaryDirectory() as tmpdir:
        tm = TaskManager(Path(tmpdir) / "tasks.json")
        task = tm.add("To delete")
        
        tm.delete(task.id)
        assert len(tm.tasks) == 0


def test_complete_task():
    with TemporaryDirectory() as tmpdir:
        tm = TaskManager(Path(tmpdir) / "tasks.json")
        task = tm.add("To complete")
        
        tm.complete(task.id)
        completed = tm._find_task(task.id)
        assert completed.status == "completed"


def test_list_filters():
    with TemporaryDirectory() as tmpdir:
        tm = TaskManager(Path(tmpdir) / "tasks.json")
        tm.add("Task 1", "high")
        tm.add("Task 2", "low")
        t3 = tm.add("Task 3", "high")
        tm.complete(t3.id)
        
        high_tasks = tm.list_tasks(priority="high")
        assert len(high_tasks) == 2
        
        completed = tm.list_tasks(status="completed")
        assert len(completed) == 1
        assert completed[0].title == "Task 3"


def test_persistence():
    with TemporaryDirectory() as tmpdir:
        storage = Path(tmpdir) / "tasks.json"
        
        tm1 = TaskManager(storage)
        tm1.add("Persisted task", "high")
        
        tm2 = TaskManager(storage)
        assert len(tm2.tasks) == 1
        assert tm2.tasks[0].title == "Persisted task"


def test_invalid_priority():
    with TemporaryDirectory() as tmpdir:
        tm = TaskManager(Path(tmpdir) / "tasks.json")
        try:
            tm.add("Task", "invalid")
            assert False, "Should raise ValueError"
        except ValueError as e:
            assert "priority" in str(e).lower()


if __name__ == "__main__":
    test_add_task()
    test_add_empty_title_fails()
    test_edit_task()
    test_delete_task()
    test_complete_task()
    test_list_filters()
    test_persistence()
    test_invalid_priority()
    print("✓ All tests passed")
