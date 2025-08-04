import json
from input_listeners.email_watcher import fetch_unread_emails
from processors.lead_parser import extract_lead
from control.notifier import notify
from email_sender import send_email_response
from creators.autoresponder import generate_response  # This is your function

def run():
    print("✅ Script started running")

    emails = fetch_unread_emails()
    print(f"📥 {len(emails)} unread email(s) fetched")

    for email_data in emails:
        print(f"\n📨 Raw Email Data:\n{email_data}")
        summary = extract_lead(email_data)
        print(f"\n📋 Summary:\n{summary}")

        reply = generate_response(summary, original_message=email_data['body'])
        print(f"\n✍️ Generated Reply:\n{reply}")

        send_email_response(
        to_email=summary['email'],
        subject=f"Re: {summary['interest_summary']}",
        body=reply
        )

        notify(summary['email'], summary['interest_summary'])

        print(f"[LOGGED] New interaction saved.\n")

if __name__ == "__main__":
    run()
