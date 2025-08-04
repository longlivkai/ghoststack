import json
from input_listeners.email_watcher import fetch_unread_emails
from processors.lead_parser import extract_lead
from creators.autoresponder import generate_response
from control.notifier import notify
from email_sender import send_email_response

def run():
    print("📥 Checking inbox...")
    emails = fetch_unread_emails()

    if not emails:
        print("📭 No unread emails found.")
        return

    print(f"📨 {len(emails)} unread email(s) found.")

    for email_data in emails:
        print("\n📨 Raw Email Data:\n", email_data)
        try:
            summary = extract_lead(email_data)  # already a dict
            print("📋 Summary:\n", summary)

            response = generate_response(summary)  # accepts dict now

            send_email_response(
                to_email=summary["email"],
                subject = "Re: " + str(summary.get("interest_summary", "your message")),
                body=response
            )

            notify(summary)  # pass dict directly if notify accepts it

        except Exception as e:
            print("❌ Error during processing:", e)

if __name__ == "__main__":
    run()
