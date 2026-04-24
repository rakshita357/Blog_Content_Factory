from utils.llm import call_llm

def run_seo_agent(blog_post, keywords):

    prompt = f"""
Give SEO suggestions for this blog:

{blog_post.get("body","")[:1500]}

Return bullet points.
"""

    text = call_llm(prompt)

    return {
        "seo_score": 8,
        "improvements": text.split("\n")
    }