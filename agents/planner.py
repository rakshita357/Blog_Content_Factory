from utils.llm import call_llm

def run_planner_agent(topic, tone):

    prompt = f"""
Create blog title and outline.

Topic: {topic}
Tone: {tone}

Return:
Title
5 headings
"""

    text = call_llm(prompt)

    return {
        "status": "success",
        "title": topic,
        "outline": text,
        "search_queries": [topic]
    }