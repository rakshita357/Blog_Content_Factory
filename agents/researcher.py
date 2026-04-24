import os
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()


def run_research_agent(search_queries, topic):
    """
    Research agent using Tavily search API
    """

    tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

    all_facts = []
    all_sources = []

    for query in search_queries:
        try:
            results = tavily.search(
                query=query,
                max_results=3
            )

            for r in results.get("results", []):

                # collect facts
                all_facts.append({
                    "fact": r.get("content", ""),
                    "source": r.get("title", "")
                })

                # collect sources
                all_sources.append({
                    "title": r.get("title", ""),
                    "url": r.get("url", ""),
                    "snippet": r.get("content", "")[:200]
                })

        except Exception as e:
            print("Tavily error:", e)

    return {
        "status": "success",
        "facts": all_facts[:10],
        "sources": all_sources[:5],
        "queries_run": search_queries
    }