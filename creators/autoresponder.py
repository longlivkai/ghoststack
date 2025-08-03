from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(prompt):
    response = client.chat.completions.create(
        model="llama3-8b-8192",  # ✅ use a valid Groq model like llama3 or gemma
        messages=[
            {"role": "system", "content": "You are an AI autoresponder. Respond clearly and concisely."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
