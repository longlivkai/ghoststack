from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_lead(email_data):
    prompt = f"""
You are a CRM assistant. Extract key lead information from the email below.

Return in JSON format with these fields:
- name
- email
- phone (if any)
- company (if any)
- interest_summary (brief summary of what the lead wants)

Email:
{email_data}
"""

    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {"role": "system", "content": "You are a lead extractor AI assistant."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.3
    )

    content = response.choices[0].message.content.strip()

    # You can later convert this to a dict using json.loads if needed
    return content
