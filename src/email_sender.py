"""
Email sending module for AutomateX.

Provides a unified interface for sending email notifications.
In development mode (APP_ENV != 'production') it falls back to printing
the message to stdout instead of connecting to an SMTP server.
"""

import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config.settings import SMTP_HOST, SMTP_PORT, EMAIL_ADDRESS, EMAIL_PASSWORD, APP_ENV

logger = logging.getLogger(__name__)


def send_email(to: str, subject: str, body: str) -> None:
    """Send an email notification.

    In development mode the email is printed to stdout as a fallback.
    In production mode the email is sent via SMTP using the credentials
    defined in the application configuration.

    Args:
        to: Recipient email address.
        subject: Email subject line.
        body: Plain-text email body.
    """
    if APP_ENV != "production":
        _print_email(to, subject, body)
        return

    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = to
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, to, msg.as_string())

        logger.info("Email sent to %s | Subject: %s", to, subject)
    except smtplib.SMTPException as exc:
        logger.error("Failed to send email to %s: %s", to, exc)
        _print_email(to, subject, body)


def _print_email(to: str, subject: str, body: str) -> None:
    """Print email details to stdout (development fallback).

    Args:
        to: Recipient email address.
        subject: Email subject line.
        body: Plain-text email body.
    """
    print(f"تنبيه: إرسال إلى {to}\nالعنوان: {subject}\nالرسالة: {body}\n")
