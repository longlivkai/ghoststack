def generate_response(summary, tone="friendly"):
    from textwrap import dedent

    name = summary.get("name", "the sender")
    interest = summary.get("interest_summary", "their inquiry")

    tone_prompt = {
        "friendly": "Use a warm, polite, and welcoming tone.",
        "professional": "Use a formal, respectful, and business-like tone.",
        "casual": "Use a relaxed, friendly, and conversational tone.",
    }.get(tone, "Use a clear, helpful tone.")

    prompt = dedent(f"""
    You are an AI assistant responding to a lead.

    The sender's name is: {name}
    They are interested in: "{interest}"

    {tone_prompt}
    
    Write a short and appropriate email response:
    - Thank them for reaching out.
    - Acknowledge their request.
    - Mention that you'll get back to them shortly.
    - Sign off as "Malakai".

    Do not repeat their message.
    Do not overpromise.
    Only output the email body.
    """)

    response = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {"role": "system", "content": "You are a helpful AI autoresponder for a tech service business."},
            {"role": "user", "content": prompt},
        ],
        temperature=0.6
    )

    return response.choices[0].message.content.strip()
