# AutomateX

**AutomateX** is a Python-based task automation system for managing deadlines and sending notifications. It supports recurring task creation and email alerts for upcoming or overdue tasks.

---

**AutomateX** هو نظام أتمتة المهام مبني بلغة Python لإدارة المواعيد النهائية وإرسال التنبيهات. يدعم إنشاء المهام الدورية وإرسال تنبيهات البريد الإلكتروني للمهام القادمة أو المتأخرة.

---

## ✨ Features / المميزات

- 📋 **Task Deadline Checking** – Automatically notifies assignees when a task deadline is within 24 hours
- 🔁 **Recurring Task Creation** – Generate periodic tasks for multiple users with configurable intervals
- 📧 **Email Notifications** – Real SMTP email sending with a fallback to console output
- ⚙️ **Configuration via `.env`** – All sensitive settings loaded from environment variables
- 🗄️ **External Task Data** – Tasks stored in `data/tasks.json`, not hardcoded
- 🧪 **Unit Tests** – Full test coverage with pytest

---

## 🚀 Installation / التثبيت

```bash
# 1. Clone the repository
git clone https://github.com/khaliiid501/AutomateX.git
cd AutomateX

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate      # Linux/macOS
venv\Scripts\activate         # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy and configure environment variables
cp .env.example .env
# Edit .env with your SMTP credentials
```

---

## ⚙️ Configuration / الإعدادات

Edit the `.env` file (created from `.env.example`):

```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_app_password
TASK_FILE_PATH=data/tasks.json
```

If `SMTP_EMAIL` and `SMTP_PASSWORD` are not set, notifications will be printed to the console instead.

---

## 📖 Usage / الاستخدام

### Check task deadlines / التحقق من المواعيد

```bash
python -m src.task_notifier
```

### Create recurring tasks / إنشاء مهام دورية

```bash
python -m src.create_recurring_tasks
```

### Programmatic usage / الاستخدام البرمجي

```python
from src.task_notifier import check_task_deadlines, load_tasks_from_json
from src.create_recurring_tasks import create_recurring_tasks

# Load tasks from JSON and send notifications
tasks = load_tasks_from_json("data/tasks.json")
check_task_deadlines(tasks)

# Create recurring tasks for a list of users
users = [
    {"name": "Ali", "email": "ali@example.com"},
    {"name": "Noor", "email": "noor@example.com"},
]
new_tasks = create_recurring_tasks(users, "Weekly Report", interval_days=7)
```

---

## 🗂️ Project Structure / هيكل المشروع

```
AutomateX/
├── src/
│   ├── __init__.py
│   ├── task_notifier.py          # Deadline checking & notifications
│   ├── create_recurring_tasks.py # Recurring task generation
│   └── email_sender.py           # Email sending (SMTP + fallback)
├── tests/
│   ├── __init__.py
│   ├── test_task_notifier.py     # Tests for task notifier
│   └── test_recurring_tasks.py   # Tests for recurring tasks
├── config/
│   ├── __init__.py
│   └── settings.py               # Environment-based configuration
├── data/
│   └── tasks.json                # Sample task data
├── .github/
│   └── workflows/
│       └── ci.yml                # GitHub Actions CI
├── .env.example                  # Environment variable template
├── .gitignore
├── README.md
├── requirements.txt
└── LICENSE
```

---

## 🧪 Running Tests / تشغيل الاختبارات

```bash
pytest tests/ -v
```

---

## 🤝 Contributing / المساهمة

Contributions are welcome! Please open an issue or submit a pull request.

---

## 📜 License / الرخصة

This project is licensed under the **MIT License** – see the [LICENSE](LICENSE) file for details.