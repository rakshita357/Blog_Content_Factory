# utils/llm.py

import os
from groq import Groq
from dotenv import load_dotenv

# load .env file
load_dotenv()

# get api key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in .env file")

# create client
client = Groq(api_key=GROQ_API_KEY)


def call_llm(prompt, model="llama3-70b-8192", temperature=0.7):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert blog writing AI that produces structured, SEO optimized content."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=temperature,
            max_tokens=2000,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"LLM Error: {str(e)}"