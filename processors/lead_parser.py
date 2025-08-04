from groq import Groq
import os
import re
import json

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_lead(email_data):
    prompt = f"""
You are a CRM assistant. Extract key lead information from the email below.

Return only in raw JSON format with these fields:
- name
- email
- phone (if any)
- company (if any)
- interest_summary (brief summary of what the lead wants)

Email:
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

    # Extract JSON using regex
    json_match = re.search(r"{.*}", content, re.DOTALL)
    if json_match:
        try:
            return json.loads(json_match.group())
        except json.JSONDecodeError as e:
            print("❌ Failed to parse JSON:", e)
            raise
    else:
        raise ValueError("❌ No valid JSON found in AI response.")
