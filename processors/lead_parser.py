from groq import Groq
import os
import re
import json

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_lead(email_data):
    print("🧠 [lead_parser] Extracting lead info...")
    prompt = f"""
You are a CRM assistant. Analyze the following email and extract only the most essential lead information.

Return a raw JSON object with these fields:
- name: Full name of the sender
- email: Email address of the sender
- phone: Phone number mentioned in the email (if any)
- company: Name of their company (if mentioned), else "Unknown"
- interest_summary: A short, one-line summary of what the sender is requesting — DO NOT repeat the exact wording of their email.

Example format:
{{
  "name": "Jane Doe",
  "email": "jane@example.com",
  "phone": "0540000000",
  "company": "Acme Ltd",
  "interest_summary": "Wants a website built for her retail business"
}}

Here is the email:
{email_data}
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a lead extractor AI assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3
    )

    content = response.choices[0].message.content.strip()

    # Extract the JSON object from the response
    json_match = re.search(r"{.*}", content, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError as e:
            print("❌ Failed to parse JSON:", e)
            raise
    else:
        raise ValueError("❌ No valid JSON found in AI response.")
