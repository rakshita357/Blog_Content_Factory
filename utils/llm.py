import streamlit as st
from groq import Groq

# Create Groq client using Streamlit secrets
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

def call_llm(prompt, temperature=0.7):
    """
    Call GROQ LLM
    """

    try:
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

    except Exception as e:
        return f"Error: {str(e)}"