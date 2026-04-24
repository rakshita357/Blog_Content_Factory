Version: 1.0
Date: 2026-04-24
Project: Blog Content Factory (Agentic Pipeline)

1) Purpose

Define the complete workflow of the system: convert a simple user input (topic + tone) into a fully structured, SEO-optimized, and evaluated blog post using a multi-agent pipeline.


2) Scope
---->> In Scope:
Blog generation from topic + tone
Multi-agent pipeline (Planner → Research → Writer → Judge)
SEO-optimized structured output
Quality scoring using LLM-as-Judge
Modular and traceable pipeline execution
--->>> Out of Scope:
Real-time publishing to CMS (WordPress, etc.)
Plagiarism detection tools
Multi-language blog generation (future scope)


3) Global Input Contract

Required Inputs:

{
  "topic": "Artificial Intelligence in Healthcare",
  "tone": "Professional",
  "word_count": 800
}


4) Global Output Contract
{
  "title": "...",
  "blog_body": "...",
  "meta_description": "...",
  "word_count": 812,
  "evaluation": {
    "accuracy": 8,
    "readability": 9,
    "seo": 7,
    "structure": 8,
    "depth": 7,
    "overall": 7.8
  }
}


 5) Task Decomposition (Agent Pipeline)
Agent 1 — Orchestrator

Goal:
Control full workflow and manage data flow between agents

Input:
User input (topic, tone, word count)

Output:
Final structured blog + evaluation

Responsibilities:

Call agents in sequence
Maintain pipeline state
Handle failures

Failure Handling:
Returns:

{
  "status": "error",
  "agent": "Agent Name",
  "message": "Failure reason"
}

Agent 2 — Topic Planner

Goal:
Generate blog structure and research direction

Input:

{
  "topic": "...",
  "tone": "..."
}

Output:

{
  "title": "...",
  "outline": ["H2 1", "H2 2"],
  "search_queries": ["query1", "query2"],
  "keywords": ["AI healthcare", "future AI"]
}

Responsibilities:

Create blog outline
Generate SEO keywords
Define research queries

Failure Handling:
Fallback → simple 5-section generic blog structure

Agent 3 — Research Agent

Goal:
Fetch relevant facts from web sources

Input:

{
  "search_queries": [...],
  "topic": "..."
}

Output:

{
  "facts": ["fact1", "fact2"],
  "sources": [
    {"title": "...", "url": "...", "snippet": "..."}
  ]
}

Responsibilities:

Perform web search (Tavily)
Extract key insights

Failure Handling:

If API fails → fallback to LLM knowledge
Log warning

Agent 4 — Writer Agent

Goal:
Generate full blog content

Input:

{
  "outline": {...},
  "facts": [...],
  "tone": "...",
  "word_count": 800
}

Output:

{
  "title": "...",
  "body": "...(markdown)...",
  "meta_description": "...",
  "word_count": 810
}

Responsibilities:

Write structured blog
Maintain tone consistency
Apply SEO formatting

Failure Handling:

Retry once with simplified prompt

Agent 5 — Judge Agent (LLM-as-Judge)

Goal:
Evaluate blog quality

Input:

{
  "blog_post": "...",
  "topic": "...",
  "research_facts": [...]
}

Output:

{
  "scores": {
    "accuracy": 8,
    "readability": 9,
    "seo": 7,
    "structure": 8,
    "depth": 7
  },
  "overall": 7.8,
  "feedback": "..."
}

Responsibilities:

Score across 5 dimensions
Provide improvement feedback

Failure Handling:
Return default:

{
  "overall": 5,
  "feedback": "evaluation failed"
}


 6) Workflow Summary
User Input
   ↓
Orchestrator
   ↓
Planner → Research → Writer → Judge
   ↓
Final Blog + Score
7) Failure & Fallback Strategy
--->Planner Agent Failure:
If the planner fails to generate a structured outline, the system falls back to a default 5-section generic blog structure.
--->Research Agent Failure:
If the web search (Tavily API) fails or returns insufficient data, the system continues using the language model’s internal knowledge to generate content.
----.Writer Agent Failure:
If the generated blog content is malformed or incomplete, the system retries once with a simplified prompt to ensure valid output.
--->Judge Agent Failure:
If evaluation fails, the system assigns a default score (e.g., overall score of 5) along with a message indicating evaluation failure.
--->API Failure (General):
If any external API fails, the system does not stop execution and instead continues the pipeline using predefined fallback mechanisms.

8) Non-Functional Requirements
Modular agent design
Low latency (optimized pipeline)
Scalable architecture
Error-resilient execution

9) Acceptance Criteria
All 5 agents execute sequentially
Blog is structured + readable
SEO elements present
Evaluation scores generated
System handles failures gracefully