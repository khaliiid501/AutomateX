from datetime import datetime, timedelta

from src.create_recurring_tasks import create_recurring_tasks


def test_create_recurring_tasks_multiple_users():
    """Test that tasks are created for each user in the list."""
    users = [
        {"name": "Ali", "email": "ali@example.com"},
        {"name": "Noor", "email": "noor@example.com"},
    ]
    tasks = create_recurring_tasks(users, "مهمة أسبوعية", 7)

    assert len(tasks) == 2
    assignees = [t["assignee"] for t in tasks]
    assert "ali@example.com" in assignees
    assert "noor@example.com" in assignees
    for task in tasks:
        assert task["name"] == "مهمة أسبوعية"


def test_create_recurring_tasks_deadline_interval():
    """Test that task deadlines match the requested interval."""
    users = [{"name": "Test User", "email": "test@example.com"}]
    before = datetime.now()
    tasks = create_recurring_tasks(users, "مهمة", 14)
    after = datetime.now()

    assert len(tasks) == 1
    deadline = tasks[0]["deadline"]
    assert before + timedelta(days=14) <= deadline <= after + timedelta(days=14)


def test_create_recurring_tasks_empty_users():
    """Test that an empty user list returns an empty task list."""
    tasks = create_recurring_tasks([], "مهمة", 7)
    assert tasks == []


def test_create_recurring_tasks_single_user():
    """Test that a single user receives exactly one task."""
    users = [{"name": "Sara", "email": "sara@example.com"}]
    tasks = create_recurring_tasks(users, "تقرير يومي", 1)

    assert len(tasks) == 1
    assert tasks[0]["assignee"] == "sara@example.com"
    assert tasks[0]["name"] == "تقرير يومي"


def test_create_recurring_tasks_various_intervals():
    """Test task creation with different interval values."""
    users = [{"name": "Ahmed", "email": "ahmed@example.com"}]

    for days in [1, 7, 30, 365]:
        before = datetime.now()
        tasks = create_recurring_tasks(users, "مهمة", days)
        after = datetime.now()

        assert len(tasks) == 1
        deadline = tasks[0]["deadline"]
        assert before + timedelta(days=days) <= deadline <= after + timedelta(days=days)
