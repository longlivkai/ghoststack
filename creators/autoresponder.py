from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_response(email_data):
    prompt = f"""
    Write a polite, professional response to this inquiry:
    Subject: {email_data['subject']}
    From: {email_data['from']}
    Body: {email_data['body']}

    Offer a follow-up or request more information if needed.
    """
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()
