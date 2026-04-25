# Blog Content Factory

> A production-style multi-agent AI system that generates high-quality, SEO-optimized blog posts from a single topic input.

The system mimics a professional content team — each step (planning, research, writing, SEO optimization, and evaluation) is handled by a specialized agent in a structured pipeline.


## What It Does

Writing a good blog post requires multiple distinct skills working in sequence. This project automates the entire workflow using an agentic architecture, ensuring faster, more consistent, and higher-quality output than a single monolithic prompt ever could.



## Pipeline

User Input (Topic + Tone)
         ↓
    Orchestrator
         ↓
  Planner → Research → Writer → SEO → Judge
         ↓
 Final Blog + Quality Score

| Stage | Agent | Responsibility |
|-------|-------|----------------|
| 1 | **Topic Planner** | Generates title, outline, keywords, and search queries |
| 2 | **Research Agent** | Fetches real-time data and facts using Tavily |
| 3 | **Writer Agent** | Generates full blog content in structured format |
| 4 | **SEO Optimizer** | Improves keyword usage, readability, and structure |
| 5 | **Judge Agent** | Evaluates blog quality and returns a final score |

---

## Agent Architecture

### Orchestrator
- Controls the full pipeline end-to-end
- Passes structured data between agents
- Handles failures and triggers fallbacks

### Topic Planner
- Generates blog structure and outline
- Creates targeted SEO keywords
- Defines research queries for the next stage

### Research Agent
- Fetches real-time information via Tavily API
- Extracts relevant facts and sources

### Writer Agent
- Writes the full blog post
- Maintains consistent tone and structure throughout

### SEO Optimizer
- Evaluates keyword density
- Improves readability and formatting

### Judge Agent *(LLM-as-Judge)*
- Scores the blog across 5 dimensions
- Provides qualitative feedback and a final verdict

---

## Failure & Fallback Strategy

Every agent has a defined fallback so the pipeline never fully breaks:

| Agent | Fallback Behavior |
|-------|-------------------|
| Planner | Uses a default 5-section blog structure |
| Research | Falls back to model's internal knowledge |
| Writer | Retries with a simplified prompt |
| SEO | Assigns default SEO scores |
| Judge | Returns a default evaluation score |
| API failure | Pipeline continues using fallback logic |

---

## Evaluation Rubric

The Judge Agent scores each blog across these dimensions:

| Criterion | Description |
|-----------|-------------|
| Accuracy | Correctness of information |
| Readability | Clarity and engagement |
| SEO | Keyword optimization |
| Structure | Logical organization |
| Depth | Topic coverage |

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11+ | Core runtime |
| Streamlit | Interactive UI |
| Gemini API | Content generation |
| Tavily API | Real-time web research |
| Plotly | Score visualization |
| python-dotenv | Environment management |

---

## Quick Start

### 1. Clone the Repository
git clone <your-repo-url>
cd blog-content-factory


### 2. Install Dependencies
python -m venv venv
venv\Scripts\activate       # Windows
# source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt


### 3. Set Up Environment Variables

Create a `.env` file in the root directory:
GEMINI_API_KEY=your_gemini_api_key
TAVILY_API_KEY=your_tavily_api_key


### 4. Run the Application

streamlit run app.py

Then open your browser at: `http://localhost:8501`

---

## Features

- Generate a full blog post from a simple topic input
- Tone selection (Professional, Casual, Academic, etc.)
- Adjustable target word count
- Real-time research integration
- SEO analysis and optimization
- Quality scoring with visual charts
- Markdown download support

---

## Project Structure

```
blog-content-factory/
│
├── app.py                        # Streamlit entry point
├── run.py                        # CLI runner
│
├── agents/
│   ├── orchestrator.py           # Pipeline controller
│   ├── planner.py                # Topic planning agent
│   ├── researcher.py             # Web research agent
│   ├── writer.py                 # Blog writing agent
│   ├── seo.py                    # SEO optimization agent
│   └── judge.py                  # Quality evaluation agent
│
├── utils/
│   └── helpers.py
│
├── submission/
│   ├── problem_statement.md
│   ├── architecture.md
│   ├── task_decomposition.md
│   └── demo.md
│
├── requirements.txt
├── .env                          # Not committed — add your keys here
└── README.md

---

Deployment (Streamlit Cloud)

1.Push the repo to GitHub
2.Open Streamlit Cloud
3.Connect your repository
4.Add API keys under App Settings → Secrets
5.Deploy
---

## Security Notes

- Never commit your `.env` file
- Keep API keys private
- Use API quotas and rate limits to avoid unexpected charges

---

## Troubleshooting

**No output generated**
- Verify your `.env` file exists and contains valid keys

**Tavily not returning results**
- Check your Tavily API key and internet connection

**Slow execution**
- Reduce topic complexity or lower the target word count

---

## Documentation

For a deeper look at the internals, see the `/submission` folder:

- `problem_statement.md` — what the project solves and why
- `architecture.md` — system design and agent interaction diagram
- `task_decomposition.md` — how the pipeline breaks down tasks
- `demo.md` — walkthrough of the system in action

---

## Key Highlights

- Modular multi-agent architecture — each agent has a single responsibility
- Real-time research integration via Tavily
- SEO-aware content generation built into the pipeline
- LLM-as-Judge evaluation with quantified scoring
- Graceful fallbacks at every stage — the pipeline never fully fails
- Clean Streamlit UI with visualization support

---

*This project demonstrates how agentic AI systems can decompose complex tasks into structured, specialized steps — enabling efficient, scalable, and high-quality content generation at speed.*
