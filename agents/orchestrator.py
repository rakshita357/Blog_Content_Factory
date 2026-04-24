from agents.planner import run_planner_agent
from agents.researcher import run_research_agent
from agents.writer import run_writer_agent
from agents.seo import run_seo_agent
from agents.judge import run_judge_agent


def run_pipeline(topic, tone, word_count=800):

    # planner
    planner = run_planner_agent(topic, tone)

    # research
    research = run_research_agent(
        planner.get("search_queries", [topic]),
        topic
    )

    # writer
    writer = run_writer_agent(
        outline=planner,
        research=research,
        tone=tone,
        word_count=word_count
    )

    # seo
    seo = run_seo_agent(
        blog_post=writer,
        keywords=[]
    )

    # judge
    judge = run_judge_agent(
        blog_post=writer,
        topic=topic,
        research_facts=research.get("facts", [])
    )

    return {
        "planner": planner,
        "research": research,
        "writer": writer,
        "seo": seo,
        "judge": judge
    }