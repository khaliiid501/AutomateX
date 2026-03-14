"""إدارة إعدادات المشروع من متغيرات البيئة."""

import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # python-dotenv غير مثبت، نستخدم متغيرات البيئة المتاحة مباشرة

# إعدادات SMTP
SMTP_HOST: str = os.getenv("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
SMTP_EMAIL: str = os.getenv("SMTP_EMAIL", "")
SMTP_PASSWORD: str = os.getenv("SMTP_PASSWORD", "")

# إعدادات عامة للمشروع
TASK_FILE_PATH: str = os.getenv(
    "TASK_FILE_PATH",
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "tasks.json"),
)
