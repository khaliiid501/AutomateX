"""
Task deadline notification module for AutomateX.

Checks task deadlines and triggers email notifications for tasks that are
due within one day or are already overdue and not yet completed.
"""

import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any

from src.email_sender import send_email

logger = logging.getLogger(__name__)


def send_email_notification(email: str, subject: str, body: str) -> None:
    """Send an email notification for a task reminder.

    This function maintains backward compatibility with the original interface
    while delegating to the dedicated email sender module.

    Args:
        email: Recipient email address.
        subject: Notification subject line.
        body: Notification message body.
    """
    send_email(email, subject, body)


def check_task_deadlines(tasks: List[Dict[str, Any]]) -> None:
    """Check all tasks and notify assignees whose deadlines are approaching.

    A notification is sent when the time remaining until the deadline is less
    than or equal to one day **and** the task status is not ``"completed"``.
    Tasks that are already overdue also trigger a notification.

    Args:
        tasks: List of task dictionaries.  Each task must contain at minimum:
            - ``name`` (str): Human-readable task name.
            - ``deadline`` (datetime): Task deadline.
            - ``assignee`` (str): Assignee email address.
            - ``status`` (str): Current task status.
    """
    current_time = datetime.now()
    for task in tasks:
        time_remaining = task["deadline"] - current_time
        if time_remaining <= timedelta(days=1) and task["status"] != "completed":
            logger.info(
                "Notifying %s about task '%s' (deadline: %s)",
                task["assignee"],
                task["name"],
                task["deadline"],
            )
            send_email_notification(
                task["assignee"],
                f"تذكير: الموعد النهائي لمهمة {task['name']} يقترب!",
                f"الموعد النهائي لهذه المهمة سيكون في {task['deadline']}. يُرجى إكمالها.",
            )
