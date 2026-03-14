# AutomateX 🤖

> **أتمتة إدارة المهام والتنبيهات** | **Task Management & Notification Automation**

[![CI](https://github.com/khaliiid501/AutomateX/actions/workflows/ci.yml/badge.svg)](https://github.com/khaliiid501/AutomateX/actions/workflows/ci.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.9+](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://www.python.org/)

---

## 🌐 الوصف | Description

### العربية
**AutomateX** هو نظام أتمتة لإدارة المهام وإرسال التنبيهات. يقوم بمراقبة المواعيد النهائية للمهام وإرسال إشعارات بريد إلكتروني تلقائية للمسؤولين عنها قبل انتهاء المواعيد، كما يدعم إنشاء مهام دورية متكررة.

### English
**AutomateX** is a Python-based task management automation system. It monitors task deadlines and automatically sends email notifications to assignees when deadlines are approaching. It also supports generating recurring tasks for teams.

---

## ✨ الميزات | Features

| الميزة | Feature |
|--------|---------|
| 📅 فحص المواعيد النهائية | Deadline monitoring |
| 📧 إشعارات بريد إلكتروني | Email notifications (SMTP + dev fallback) |
| 🔄 مهام دورية متكررة | Recurring task generation |
| 🗄️ بيانات خارجية (JSON) | Externalized task data (JSON) |
| ⚙️ إعدادات عبر متغيرات البيئة | Environment-variable-based configuration |
| 📝 Logging شامل | Structured logging throughout |
| 🧪 اختبارات وحدة | Full unit test suite |
| 🔄 CI/CD تلقائي | Automated CI via GitHub Actions |

---

## 🏗️ هيكل المشروع | Project Structure

```
AutomateX/
├── src/
│   ├── __init__.py                # Package init
│   ├── task_notifier.py           # Deadline checking & notification logic
│   ├── create_recurring_tasks.py  # Recurring task generation
│   └── email_sender.py            # Email sending (SMTP / dev fallback)
├── tests/
│   ├── __init__.py
│   ├── test_task_notifier.py      # Tests for task_notifier
│   └── test_recurring_tasks.py    # Tests for create_recurring_tasks
├── config/
│   └── settings.py                # Centralised configuration (env vars)
├── data/
│   └── tasks.json                 # Externalized task data
├── .github/
│   └── workflows/
│       └── ci.yml                 # GitHub Actions CI workflow
├── .env.example                   # Environment variable template
├── .gitignore
├── main.py                        # Application entry point
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 🚀 التثبيت والتشغيل | Installation & Usage

### 1. استنساخ المستودع | Clone the repository

```bash
git clone https://github.com/khaliiid501/AutomateX.git
cd AutomateX
```

### 2. إنشاء بيئة افتراضية | Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux / macOS
.venv\Scripts\activate      # Windows
```

### 3. تثبيت الاعتماديات | Install dependencies

```bash
pip install -r requirements.txt
```

### 4. إعداد متغيرات البيئة | Configure environment variables

```bash
cp .env.example .env
# Edit .env and fill in your SMTP credentials
```

### 5. تشغيل التطبيق | Run the application

```bash
python main.py
```

---

## ⚙️ الإعدادات | Configuration

Copy `.env.example` to `.env` and set the following variables:

| المتغير | Variable | الوصف | Description | الافتراضي | Default |
|---------|----------|--------|-------------|-----------|---------|
| `SMTP_HOST` | SMTP Host | خادم SMTP | SMTP server hostname | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP Port | منفذ SMTP | SMTP server port | `587` |
| `EMAIL_ADDRESS` | Sender email | بريد المرسل | Sender email address | _(empty)_ |
| `EMAIL_PASSWORD` | Email password | كلمة مرور البريد | Sender email password | _(empty)_ |
| `APP_ENV` | App environment | بيئة التشغيل | `development` or `production` | `development` |
| `TASKS_FILE` | Tasks file path | مسار ملف المهام | Path to tasks JSON file | `data/tasks.json` |

> **ملاحظة:** في وضع `development` يتم طباعة الإشعارات على الشاشة بدلاً من إرسالها.
> **Note:** In `development` mode notifications are printed to stdout instead of being sent.

---

## 🗄️ بيانات المهام | Task Data

Tasks are stored in `data/tasks.json`. Each task has the following structure:

```json
{
    "id": 1,
    "name": "إعداد تقارير",
    "deadline": "2026-03-15T14:00:00",
    "assignee": "ahmed@example.com",
    "status": "ongoing"
}
```

Valid status values: `"ongoing"`, `"pending"`, `"completed"`

---

## 🧪 تشغيل الاختبارات | Running Tests

```bash
pytest tests/ -v
```

---

## 🤝 المساهمة | Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/my-feature`
3. Commit your changes: `git commit -m 'Add my feature'`
4. Push to the branch: `git push origin feature/my-feature`
5. Open a Pull Request

---

## 📜 الرخصة | License

This project is licensed under the **MIT License** – see [LICENSE](LICENSE) for details.