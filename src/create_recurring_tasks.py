"""
Recurring task creation module for AutomateX.

Generates task assignments for a list of users based on a configurable
repetition interval.
"""

import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any

logger = logging.getLogger(__name__)


def create_recurring_tasks(
    users: List[Dict[str, Any]],
    task_name: str,
    interval_days: int,
) -> List[Dict[str, Any]]:
    """Create recurring tasks for a list of users.

    For each user a new task entry is created whose deadline is
    ``interval_days`` from the current date and time.

    Args:
        users: List of user dictionaries.  Each entry must contain at least:
            - ``name`` (str): User's display name.
            - ``email`` (str): User's email address.
        task_name: Name/title of the recurring task.
        interval_days: Number of days from now until the task deadline.

    Returns:
        A list of task dictionaries with the following keys:
            - ``name``: Task name (same as ``task_name``).
            - ``assignee``: Assignee email address.
            - ``deadline``: :class:`~datetime.datetime` of the task deadline.
    """
    recurring_tasks: List[Dict[str, Any]] = []
    current_time = datetime.now()
    for user in users:
        task_deadline = current_time + timedelta(days=interval_days)
        task = {
            "name": task_name,
            "assignee": user["email"],
            "deadline": task_deadline,
        }
        recurring_tasks.append(task)
        logger.info(
            "Created task '%s' for %s (deadline: %s)",
            task_name,
            user["email"],
            task_deadline,
        )
    return recurring_tasks
