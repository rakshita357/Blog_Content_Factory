import os
from dotenv import load_dotenv
from groq import Groq

# Load .env file
load_dotenv()

# ---------------- GROQ TEST ----------------
groq_key = os.getenv("GROQ_API_KEY")

if not groq_key:
    print("❌ GROQ_API_KEY not found in .env")
else:
    try:
        client = Groq(api_key=groq_key)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "user", "content": "Say hello in one sentence"}
            ]
        )

        print("✅ GROQ OK:")
        print(response.choices[0].message.content)

    except Exception as e:
        print("❌ GROQ ERROR:", e)


# ---------------- TAVILY TEST ----------------
try:
    from tavily import TavilyClient

    tavily_key = os.getenv("TAVILY_API_KEY")

    if not tavily_key:
        print("❌ TAVILY_API_KEY not found in .env")
    else:
        tavily = TavilyClient(api_key=tavily_key)

        result = tavily.search(
            "What is artificial intelligence?",
            max_results=1
        )

        print("\n✅ TAVILY OK:")
        print(result["results"][0]["title"])

except Exception as e:
    print("❌ TAVILY ERROR:", e)