import os
from groq import Groq
from dotenv import load_dotenv

# load .env
load_dotenv()

# create groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def call_llm(prompt, temperature=0.7):
    """
    Call GROQ LLM
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=2048
    )

    return response.choices[0].message.content