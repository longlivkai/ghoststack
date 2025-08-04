from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(summary, tone="friendly"):
    """
    Generate an AI response based on a lead summary.
    
    Parameters:
    - summary: dict with keys (name, email, phone, company, interest_summary)
    - tone: string – 'friendly', 'professional', or 'casual'
    """
    name = summary.get("name", "the sender")
    interest = summary.get("interest_summary", "their inquiry")

    tone_prompt = {
        "friendly": "Write in a warm, approachable tone.",
        "professional": "Write in a concise, respectful business tone.",
        "casual": "Write casually, like you're talking to a peer or friend.",
    }.get(tone, "Write in a clear and helpful tone.")

    prompt = f"""
You received an email from {name}.
Their message or interest is: "{interest}"

{tone_prompt}
Thank them for reaching out, briefly acknowledge their request, and let them know you’ll respond soon.
Sign the message as “Malakai” and avoid overpromising.
    """

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are an AI autoresponder. Respond clearly and concisely."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7
    )

    return response.choices[0].message.content.strip()
