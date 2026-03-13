from datetime import datetime, timedelta

# قائمة المهام
tasks = [
    {"id": 1, "name": "إعداد تقارير", "deadline": datetime(2026, 3, 15, 14, 0), "assignee": "ahmed@example.com", "status": "ongoing"},
    {"id": 2, "name": "اجتماع العميل", "deadline": datetime(2026, 3, 13, 18, 0), "assignee": "sara@example.com", "status": "pending"}
]

# وظيفة إرسال تنبيه
def send_email_notification(email, subject, body):
    """ترسل بريد إلكتروني للإشعار"""
    print(f"تنبيه: إرسال إلى {email}\nالعنوان: {subject}\nالرسالة: {body}\n")

# التحقق من المهام وتنبيه المتأخرين
def check_task_deadlines(tasks):
    current_time = datetime.now()
    for task in tasks:
        time_remaining = task['deadline'] - current_time

        # إذا تبقى أقل من يوم واحد
        if time_remaining <= timedelta(days=1) and task['status'] != "completed":
            send_email_notification(
                task["assignee"],
                f"تذكير: الموعد النهائي لمهمة {task['name']} يقترب!",
                f"الموعد النهائي لهذه المهمة سيكون في {task['deadline']}. يُرجى إكمالها."
            )

# تنفيذ المهمة
if __name__ == '__main__':
    check_task_deadlines(tasks)
