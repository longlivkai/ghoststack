from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(summary, tone="friendly"):
    """
    Generate an AI response based on a lead summary.
    """
    name = summary.get("name", "the sender")
    interest = summary.get("interest_summary", "their inquiry")

    tone_prompt = {
        "friendly": "Use a warm, helpful tone.",
        "professional": "Use a polite, businesslike tone.",
        "casual": "Be casual and easygoing.",
    }.get(tone, "Be helpful and clear.")

    prompt = f"""
You are a helpful assistant writing an email reply to a potential client.

The client’s name is: {name}
They expressed interest in: {interest}

{tone_prompt}
Do NOT repeat the user's email message directly.
Instead:
- Thank them for reaching out.
- Acknowledge their request.
- Let them know you'll follow up soon.
- Sign off as “Malakai”.

Avoid making promises or asking for details. Keep it short and clear.
"""

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are an AI autoresponder that replies to customer leads clearly and politely."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.5
    )

    return response.choices[0].message.content.strip()
