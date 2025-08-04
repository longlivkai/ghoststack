import json
from input_listeners.email_watcher import fetch_unread_emails
from processors.lead_parser import extract_lead

from control.notifier import notify
from email_sender import send_email_response

def generate_response(summary, tone="friendly", original_message=""):
    from groq import Groq
    import os
    from dotenv import load_dotenv
    load_dotenv()

    client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    name = summary.get("name", "the sender")
    interest = summary.get("interest_summary", "their inquiry")

    tone_prompt = {
        "friendly": "Use a warm, approachable tone.",
        "professional": "Use a concise, respectful business tone.",
        "casual": "Use a relaxed, informal tone.",
    }.get(tone, "Use a clear and helpful tone.")

    prompt = f"""
You are an assistant helping Malakai respond to leads.

Here is the original message from {name}:
\"\"\"
{original_message}
\"\"\"

Summary of the person's interest:
{interest}

Instructions:
- Write a fresh, original email reply (no paraphrasing)
- Thank the person for reaching out
- Briefly acknowledge the summary of their request
- Let them know Malakai will follow up soon
- Keep the tone: {tone_prompt}
- Sign off as “Malakai”
- **Do NOT repeat or summarize the original message directly**

Write only the email body.
"""

    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    reply_text = response.choices[0].message.content.strip()
    return reply_text
