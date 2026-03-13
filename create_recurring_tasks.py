from datetime import datetime, timedelta

# قائمة أولية بالمستخدمين والمهام الدورية
users = [
    {"name": "Ali", "email": "ali@example.com"},
    {"name": "Noor", "email": "noor@example.com"}
]

# إنشاء المهام الدورية
def create_recurring_tasks(users, task_name, interval_days):
    recurring_tasks = []
    current_time = datetime.now()
    for user in users:
        task_deadline = current_time + timedelta(days=interval_days)
        recurring_tasks.append({
            "name": task_name,
            "assignee": user["email"],
            "deadline": task_deadline
        })
    return recurring_tasks

# إنشاء المهام كل 7 أيام
tasks = create_recurring_tasks(users, "تحليل نتائج الأداء الأسبوعي", 7)

# عرض المهام
for task in tasks:
    print(f"تم تعيين مهمة '{task['name']}' لـ {task['assignee']}, الموعد النهائي: {task['deadline']}")
