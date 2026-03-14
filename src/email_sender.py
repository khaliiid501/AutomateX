"""وحدة إرسال البريد الإلكتروني لمشروع AutomateX."""

import logging
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger(__name__)


def send_email_notification(email: str, subject: str, body: str) -> None:
    """ترسل بريد إلكتروني للإشعار عبر SMTP أو تطبع على الشاشة كـ fallback.

    Args:
        email: عنوان البريد الإلكتروني للمستلم.
        subject: عنوان الرسالة.
        body: نص الرسالة.
    """
    try:
        from config.settings import SMTP_HOST, SMTP_PORT, SMTP_EMAIL, SMTP_PASSWORD

        if SMTP_EMAIL and SMTP_PASSWORD:
            msg = MIMEMultipart()
            msg["From"] = SMTP_EMAIL
            msg["To"] = email
            msg["Subject"] = subject
            msg.attach(MIMEText(body, "plain", "utf-8"))

            with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
                server.starttls()
                server.login(SMTP_EMAIL, SMTP_PASSWORD)
                server.sendmail(SMTP_EMAIL, email, msg.as_string())

            logger.info("تم إرسال البريد الإلكتروني إلى %s بنجاح", email)
            return
    except Exception as exc:  # noqa: BLE001
        logger.warning("فشل إرسال البريد عبر SMTP: %s", exc)

    # Fallback: طباعة الإشعار على الشاشة
    print(f"تنبيه: إرسال إلى {email}\nالعنوان: {subject}\nالرسالة: {body}\n")
