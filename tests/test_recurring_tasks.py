"""
Tests for the create_recurring_tasks module.

Validates recurring task generation logic.
"""

from datetime import datetime, timedelta

import pytest

from src.create_recurring_tasks import create_recurring_tasks


def test_create_recurring_tasks_returns_correct_count():
    """Each user should receive exactly one task."""
    users = [
        {"name": "Ali", "email": "ali@example.com"},
        {"name": "Noor", "email": "noor@example.com"},
    ]
    tasks = create_recurring_tasks(users, "Weekly Report", 7)
    assert len(tasks) == 2


def test_create_recurring_tasks_assigns_correct_emails():
    """Each task should be assigned to the corresponding user email."""
    users = [
        {"name": "Ali", "email": "ali@example.com"},
        {"name": "Noor", "email": "noor@example.com"},
    ]
    tasks = create_recurring_tasks(users, "Weekly Report", 7)
    assignees = [t["assignee"] for t in tasks]
    assert "ali@example.com" in assignees
    assert "noor@example.com" in assignees


def test_create_recurring_tasks_correct_deadline_interval():
    """Task deadline should be approximately interval_days from now."""
    users = [{"name": "Ali", "email": "ali@example.com"}]
    before = datetime.now()
    tasks = create_recurring_tasks(users, "Report", 5)
    after = datetime.now()

    deadline = tasks[0]["deadline"]
    assert before + timedelta(days=5) <= deadline <= after + timedelta(days=5)


def test_create_recurring_tasks_correct_name():
    """All tasks should have the supplied task name."""
    users = [{"name": "Ali", "email": "ali@example.com"}]
    tasks = create_recurring_tasks(users, "تحليل نتائج الأداء", 3)
    assert tasks[0]["name"] == "تحليل نتائج الأداء"


def test_create_recurring_tasks_empty_users():
    """An empty user list should return an empty task list."""
    tasks = create_recurring_tasks([], "No Task", 7)
    assert tasks == []


def test_create_recurring_tasks_zero_interval():
    """An interval of 0 days means the deadline is roughly now."""
    users = [{"name": "Ali", "email": "ali@example.com"}]
    before = datetime.now()
    tasks = create_recurring_tasks(users, "Immediate Task", 0)
    after = datetime.now()

    deadline = tasks[0]["deadline"]
    assert before <= deadline <= after
