from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
import sys

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    print("❌ OPENAI_API_KEY is not set", file=sys.stderr)
    raise EnvironmentError("OPENAI_API_KEY not found in environment variables")

client = OpenAI(api_key=api_key)

def extract_lead(email_data):
    prompt = f"""
    This is a raw email:
    Subject: {email_data['subject']}
    From: {email_data['from']}
    Body: {email_data['body']}

    Is this a potential client inquiry? If yes, extract their name, intent, and suggested response.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
