from groq import Groq

client = Groq(api_key="GROQ_API_KEY")  # or use an environment variable

def generate_response(prompt):
    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",  # or another model like llama3-8b or gemma-7b
        messages=[
            {"role": "system", "content": "You are an AI autoresponder. Respond clearly and concisely."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7
    )
    return response.choices[0].message.content.strip()
