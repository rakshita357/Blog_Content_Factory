import streamlit as st
import time
from agents.orchestrator import run_pipeline

# Page config
st.set_page_config(
    page_title="Blog Content Factory",
    page_icon="📰",
    layout="wide"
)

# Header
st.title("📰 Blog Content Factory")
st.caption("Multi-Agent AI Blog Generator (Groq + Tavily)")

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    tone = st.selectbox(
        "Tone",
        [
            "Professional",
            "Conversational",
            "Technical",
            "Friendly",
            "Educational",
            "Persuasive"
        ]
    )

    word_count = st.slider(
        "Word count",
        400,
        1500,
        800,
        step=100
    )

    st.divider()
    st.markdown("### Agents")
    st.markdown("""
    1. Planner  
    2. Research  
    3. Writer  
    4. SEO  
    5. Judge  
    """)

# Main input
topic = st.text_input(
    "Enter blog topic",
    placeholder="Example: Future of AI in Healthcare"
)

generate = st.button("🚀 Generate Blog", use_container_width=True)

# Run pipeline
if generate:

    if not topic:
        st.warning("Please enter topic")
        st.stop()

    progress = st.progress(0)
    status = st.empty()

    status.write("🧠 Planning...")
    progress.progress(20)
    time.sleep(0.3)

    status.write("🔍 Researching...")
    progress.progress(40)
    time.sleep(0.3)

    status.write("✍️ Writing...")
    progress.progress(60)
    time.sleep(0.3)

    status.write("🔎 SEO optimizing...")
    progress.progress(80)
    time.sleep(0.3)

    status.write("⚖️ Evaluating...")
    progress.progress(95)

    # Run agents
    result = run_pipeline(
        topic=topic,
        tone=tone,
        word_count=word_count
    )

    progress.progress(100)
    status.write("✅ Done")

    writer = result.get("writer", {})
    judge = result.get("judge", {})
    seo = result.get("seo", {})

    st.divider()

    # Blog output
    st.header(writer.get("title", "Generated Blog"))

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Word Count",
            writer.get("word_count", 0)
        )

    with col2:
        st.metric(
            "Score",
            judge.get("overall_score", 0)
        )

    with col3:
        st.metric(
            "SEO",
            seo.get("seo_score", 0)
        )

    st.divider()

    st.markdown(writer.get("body", ""))

    # Judge section
    st.divider()
    st.subheader("⚖️ Quality Evaluation")

    scores = judge.get("scores", {})

    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric("Accuracy", scores.get("accuracy", 0))
    col2.metric("Readability", scores.get("readability", 0))
    col3.metric("SEO", scores.get("seo_quality", 0))
    col4.metric("Structure", scores.get("structure", 0))
    col5.metric("Depth", scores.get("depth", 0))

    st.write("Verdict:", judge.get("verdict", "—"))

    # SEO section
    st.divider()
    st.subheader("🔎 SEO Suggestions")

    for i in seo.get("improvements", []):
        st.write("•", i)