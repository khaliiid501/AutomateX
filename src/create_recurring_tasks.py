"""وحدة إنشاء المهام الدورية المتكررة."""

import logging
from datetime import datetime, timedelta
from typing import Any

logger = logging.getLogger(__name__)


def create_recurring_tasks(
    users: list[dict[str, str]],
    task_name: str,
    interval_days: int,
) -> list[dict[str, Any]]:
    """ينشئ مهام دورية لقائمة من المستخدمين.

    Args:
        users: قائمة من قواميس المستخدمين، يجب أن يحتوي كل قاموس على
               المفاتيح ``name`` و ``email``.
        task_name: اسم المهمة الدورية.
        interval_days: عدد الأيام حتى الموعد النهائي للمهمة.

    Returns:
        قائمة من قواميس المهام المنشأة، تحتوي على ``name`` و ``assignee``
        و ``deadline``.
    """
    recurring_tasks: list[dict[str, Any]] = []
    current_time = datetime.now()

    for user in users:
        task_deadline = current_time + timedelta(days=interval_days)
        task: dict[str, Any] = {
            "name": task_name,
            "assignee": user["email"],
            "deadline": task_deadline,
        }
        recurring_tasks.append(task)
        logger.debug(
            "تم إنشاء مهمة '%s' للمستخدم %s، الموعد النهائي: %s",
            task_name,
            user["email"],
            task_deadline,
        )

    logger.info("تم إنشاء %d مهمة دورية بنجاح", len(recurring_tasks))
    return recurring_tasks


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)

    _users = [
        {"name": "Ali", "email": "ali@example.com"},
        {"name": "Noor", "email": "noor@example.com"},
    ]

    _tasks = create_recurring_tasks(_users, "تحليل نتائج الأداء الأسبوعي", 7)

    for _task in _tasks:
        print(
            f"تم تعيين مهمة '{_task['name']}' لـ {_task['assignee']},"
            f" الموعد النهائي: {_task['deadline']}"
        )
