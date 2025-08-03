import smtplib
from email.message import EmailMessage
import os

def send_email_response(to_email, subject, body):
    email_address = os.getenv("EMAIL")
    email_password = os.getenv("PASSWORD")

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = email_address
    msg["To"] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)
