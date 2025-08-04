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
You are an AI assistant. A potential client named {name} has reached out.

They are interested in: {interest}

Your job is to write a brief reply. DO NOT copy or repeat anything from their message. Instead:

- Thank them for reaching out.
- Acknowledge their interest in website services.
- Let them know you'll follow up soon.
- Use a {tone} tone.
- Sign off as "Malakai".

Example format:

Dear [Client Name],

Thanks for reaching out! I appreciate your interest in [service]. I'll be in touch shortly to discuss how we can move forward.

Best regards,  
Malakai

Again, DO NOT copy or paraphrase the user’s email message.
Only use the summary of their interest and name.
"""
