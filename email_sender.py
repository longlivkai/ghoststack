import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from dotenv import load_dotenv

load_dotenv()

def send_email_response(to_email, subject, body):
    print(f"📤 [email_sender] Sending email to {to_email}...")

    try:
        message = Mail(
            from_email=os.getenv("SENDER_EMAIL"),
            to_emails=to_email,
            subject=subject if subject else "Re: Your Message",
            plain_text_content=body if body else "Thank you for reaching out."
        )

        sg = SendGridAPIClient(os.getenv("SENDGRID_API_KEY"))
        response = sg.send(message)
        print(f"✅ Email sent! Status: {response.status_code}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
