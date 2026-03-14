"""وحدة التحقق من مواعيد المهام وإرسال التنبيهات."""

import json
import logging
from datetime import datetime, timedelta
from typing import Any

from src.email_sender import send_email_notification

logger = logging.getLogger(__name__)


def load_tasks_from_json(file_path: str) -> list[dict[str, Any]]:
    """تحمّل قائمة المهام من ملف JSON.

    Args:
        file_path: مسار ملف JSON الذي يحتوي على بيانات المهام.

    Returns:
        قائمة من قواميس المهام. يتم تحويل حقل deadline من نص إلى datetime.
    """
    with open(file_path, encoding="utf-8") as fh:
        raw: list[dict[str, Any]] = json.load(fh)

    for task in raw:
        if isinstance(task.get("deadline"), str):
            task["deadline"] = datetime.fromisoformat(task["deadline"])

    logger.debug("تم تحميل %d مهمة من %s", len(raw), file_path)
    return raw


def check_task_deadlines(tasks: list[dict[str, Any]]) -> None:
    """يتحقق من مواعيد المهام ويرسل تنبيهات للمهام التي اقترب موعدها.

    يتم إرسال تنبيه لأي مهمة غير مكتملة يتبقى على موعدها النهائي يوم واحد
    أو أقل (بما في ذلك المهام المتأخرة).

    Args:
        tasks: قائمة من قواميس المهام، يجب أن يحتوي كل قاموس على المفاتيح:
               ``deadline`` (datetime)، ``status`` (str)، ``assignee`` (str)،
               و ``name`` (str).
    """
    current_time = datetime.now()
    for task in tasks:
        time_remaining = task["deadline"] - current_time

        if time_remaining <= timedelta(days=1) and task["status"] != "completed":
            logger.info("تنبيه: الموعد النهائي لمهمة '%s' يقترب", task["name"])
            send_email_notification(
                task["assignee"],
                f"تذكير: الموعد النهائي لمهمة {task['name']} يقترب!",
                f"الموعد النهائي لهذه المهمة سيكون في {task['deadline']}. يُرجى إكمالها.",
            )


if __name__ == "__main__":
    from config.settings import TASK_FILE_PATH

    logging.basicConfig(level=logging.INFO)
    _tasks = load_tasks_from_json(TASK_FILE_PATH)
    check_task_deadlines(_tasks)
