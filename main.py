from input_listeners.email_watcher import fetch_unread_emails
from processors.lead_parser import extract_lead
from creators.autoresponder import generate_response
from control.notifier import notify

def run():
    print("📥 Checking inbox...")
    emails = fetch_unread_emails()

    for email_data in emails:
        print(f"🔍 Processing: {email_data['subject']}")
        summary = extract_lead(email_data)
        response = generate_response(email_data)

        output = f"""
        === LEAD SUMMARY ===
        {summary}
        --- RESPONSE DRAFT ---
        {response}
        =======================
        """
        notify(output)

if __name__ == "__main__":
    run()
