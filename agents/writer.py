from utils.llm import call_llm

def run_writer_agent(outline, research, tone, word_count=800):

    topic = outline.get("title", "Blog")

    prompt = f"""
Write a full blog post.

Topic: {topic}
Tone: {tone}
Length: {word_count} words

Write with:
- introduction
- headings
- conclusion
- markdown formatting

Return ONLY the blog content.
"""

    text = call_llm(prompt)

    return {
        "status": "success",
        "title": topic,
        "body": text,
        "word_count": len(text.split())
    }