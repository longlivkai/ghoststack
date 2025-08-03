def fetch_unread_emails():
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(EMAIL, PASSWORD)
    mail.select("inbox")

    # 🔧 This now fetches all unread emails
    _, data = mail.search(None, 'UNSEEN')
    print("📡 IMAP search result:", data)  # Debug log

    email_ids = data[0].split()
    emails = []

    for eid in email_ids:
        _, msg_data = mail.fetch(eid, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])
                subject = msg["subject"]
                from_ = msg["from"]
                body = ""
                if msg.is_multipart():
                    for part in msg.walk():
                        if part.get_content_type() == "text/plain":
                            body += part.get_payload(decode=True).decode()
                else:
                    body = msg.get_payload(decode=True).decode()

                emails.append({
                    "from": from_,
                    "subject": subject,
                    "body": body
                })

    mail.logout()
    return emails
