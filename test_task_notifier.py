from datetime import datetime, timedelta

from task_notifier import send_email_notification, check_task_deadlines


def test_send_email_notification(capsys):
    """Test that send_email_notification prints the correct output."""
    send_email_notification("test@example.com", "Test Subject", "Test Body")
    captured = capsys.readouterr()
    assert "test@example.com" in captured.out
    assert "Test Subject" in captured.out
    assert "Test Body" in captured.out


def test_check_task_deadlines_notifies_near_deadline(capsys):
    """Test that tasks with deadlines within 1 day trigger notifications."""
    now = datetime.now()
    tasks = [
        {"id": 1, "name": "Urgent Task", "deadline": now + timedelta(hours=12), "assignee": "user@example.com", "status": "ongoing"},
    ]
    check_task_deadlines(tasks)
    captured = capsys.readouterr()
    assert "user@example.com" in captured.out
    assert "Urgent Task" in captured.out


def test_check_task_deadlines_skips_completed(capsys):
    """Test that completed tasks are not notified even if deadline is near."""
    now = datetime.now()
    tasks = [
        {"id": 1, "name": "Done Task", "deadline": now + timedelta(hours=6), "assignee": "done@example.com", "status": "completed"},
    ]
    check_task_deadlines(tasks)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_check_task_deadlines_skips_far_deadline(capsys):
    """Test that tasks with deadlines more than 1 day away are not notified."""
    now = datetime.now()
    tasks = [
        {"id": 1, "name": "Future Task", "deadline": now + timedelta(days=5), "assignee": "future@example.com", "status": "pending"},
    ]
    check_task_deadlines(tasks)
    captured = capsys.readouterr()
    assert captured.out == ""


def test_check_task_deadlines_notifies_past_deadline(capsys):
    """Test that tasks past their deadline are still notified if not completed."""
    now = datetime.now()
    tasks = [
        {"id": 1, "name": "Overdue Task", "deadline": now - timedelta(hours=2), "assignee": "late@example.com", "status": "ongoing"},
    ]
    check_task_deadlines(tasks)
    captured = capsys.readouterr()
    assert "late@example.com" in captured.out
    assert "Overdue Task" in captured.out
