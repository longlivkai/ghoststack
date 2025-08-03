from input_listeners.email_watcher import fetch_unread_emails
from processors.lead_parser import extract_lead
from creators.autoresponder import generate_response
from control.notifier import notify

def run():
    print("📥 Checking inbox...")
    emails = fetch_unread_emails()

    if not emails:
        print("📭 No unread emails found.")
        return

    print(f"📨 {len(emails)} unread email(s) found.")

    for email_data in emails:
        print("\n📨 Raw Email Data:\n", email_data)  # Debug
        try:
            summary = extract_lead(email_data)
            print("📋 Summary:", summary)
            response = generate_response(summary)
            send_email_response(email_data, response)
        except Exception as e:
            print("❌ Error during processing:", e)
