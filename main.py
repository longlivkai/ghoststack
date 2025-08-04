import json  # 🔼 Add this to parse the Groq output
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
            summary_str = extract_lead(email_data)
            print("📋 Summary:\n", summary_str)

            summary = json.loads(summary_str)  # ✅ Convert to dict

            response = generate_response(json.dumps(summary))  # 🔁 Properly pass string

            send_email_response(
                to_email=summary["email"],
                subject="Re: " + (summary["interest_summary"] or "your message"),
                body=response
            )

            notify(summary_str)  # Optional: log the JSON string

        except Exception as e:
            print("❌ Error during processing:", e)

if __name__ == "__main__":
    run()
