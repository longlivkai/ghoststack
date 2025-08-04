import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY")  # Load from .env or environment

def send_email_response(to_email, subject, body):
    print(f"📤 [email_sender] Sending email to {to_email}...")

    message = Mail(
        from_email='malakaichiba09@gmail.com',
        to_emails=to_email,
        subject=subject,
        plain_text_content=body
    )

    try:
        sg = SendGridAPIClient(SENDGRID_API_KEY)
        response = sg.send(message)
        print(f"✅ Email sent! Status Code: {response.status_code}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
