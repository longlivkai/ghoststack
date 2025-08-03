import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def extract_lead(email_data):
    prompt = f"""
    This is a lead email. Extract the following info as JSON:
    - name
    - phone
    - email
    - company
    - what they’re asking for or selling

    Email content:
    \"\"\"
    {email_data}
    \"\"\"
    """

    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that extracts structured leads from email."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
