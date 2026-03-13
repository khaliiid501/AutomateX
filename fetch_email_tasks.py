import imaplib
import email
from datetime import datetime, timedelta

# بيانات تسجيل الدخول
EMAIL = "your_email@example.com"
PASSWORD = "your_password"

# تسجيل الدخول إلى البريد
def fetch_email_tasks():
    mail = imaplib.IMAP4_SSL("imap.mailserver.com")
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")

    status, messages = mail.search(None, 'UNSEEN')  # جلب الرسائل غير المقروءة
    tasks = []

    for msg_num in messages[0].split():
        _, data = mail.fetch(msg_num, '(RFC822)')
        message = email.message_from_bytes(data[0][1])

        subject = message["subject"]
        tasks.append({
            "name": subject,
            "assignee": EMAIL,
            "deadline": datetime.now() + timedelta(days=1)  # الموعد الافتراضي يوم آخر
        })

    mail.logout()
    return tasks

# عرض المهام الجديدة
new_tasks = fetch_email_tasks()
print("تم استخراج المهام: ", new_tasks)
