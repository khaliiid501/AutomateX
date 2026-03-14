"""
AutomateX – Entry point.

Loads tasks from the JSON data file and runs the deadline check,
sending notifications as needed.
"""

import json
import logging
import sys
from datetime import datetime

from config.settings import TASKS_FILE
from src.task_notifier import check_task_deadlines
from src.create_recurring_tasks import create_recurring_tasks

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def load_tasks(filepath: str):
    """Load tasks from a JSON file.

    Each task's ``deadline`` string is converted to a :class:`~datetime.datetime`
    object so it can be used directly by :func:`~src.task_notifier.check_task_deadlines`.

    Args:
        filepath: Absolute or relative path to the JSON tasks file.

    Returns:
        List of task dictionaries with parsed ``deadline`` values.
    """
    with open(filepath, "r", encoding="utf-8") as fh:
        raw_tasks = json.load(fh)

    for task in raw_tasks:
        if isinstance(task.get("deadline"), str):
            task["deadline"] = datetime.fromisoformat(task["deadline"])

    return raw_tasks


def main() -> None:
    """Main entry point: load tasks and check deadlines."""
    logger.info("AutomateX starting up…")
    try:
        tasks = load_tasks(TASKS_FILE)
        logger.info("Loaded %d task(s) from %s", len(tasks), TASKS_FILE)
    except FileNotFoundError:
        logger.error("Tasks file not found: %s", TASKS_FILE)
        sys.exit(1)
    except json.JSONDecodeError as exc:
        logger.error("Invalid JSON in tasks file: %s", exc)
        sys.exit(1)

    check_task_deadlines(tasks)
    logger.info("Deadline check complete.")


if __name__ == "__main__":
    main()
