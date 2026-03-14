"""
Centralized configuration module for AutomateX.

Reads settings from environment variables (with .env support via python-dotenv).
"""

import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# SMTP configuration
SMTP_HOST: str = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT: int = int(os.environ.get("SMTP_PORT", "587"))
EMAIL_ADDRESS: str = os.environ.get("EMAIL_ADDRESS", "")
EMAIL_PASSWORD: str = os.environ.get("EMAIL_PASSWORD", "")

# Application mode: "development" uses print-based fallback; "production" uses real SMTP
APP_ENV: str = os.environ.get("APP_ENV", "development")

# Path to the tasks data file
TASKS_FILE: str = os.environ.get(
    "TASKS_FILE",
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "tasks.json"),
)
