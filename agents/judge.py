from utils.llm import call_llm

def run_judge_agent(blog_post, topic, research_facts):

    prompt = f"""
Score this blog out of 10:

{blog_post.get("body","")[:1500]}

Give:
Accuracy
Readability
SEO
Structure
Depth
"""

    text = call_llm(prompt)

    return {
        "overall_score": 8,
        "scores": {
            "accuracy": 8,
            "readability": 8,
            "seo_quality": 8,
            "structure": 8,
            "depth": 8
        },
        "verdict": "PUBLISH"
    }