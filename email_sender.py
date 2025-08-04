import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()  # Load from .env

def send_email_response(to_email, subject, body):
    print(f"📤 [email_sender] Sending email to {to_email}...")

    message = Mail(
        from_email=os.getenv("SENDER_EMAIL"),
        to_emails=to_email,
        subject=subject,
        plain_text_content=body
    )

    try:
        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(f"✅ Email sent! Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
