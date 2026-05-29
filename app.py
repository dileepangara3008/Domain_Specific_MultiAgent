import streamlit as st
from graph import build_graph
from llm import llm
import time

# -----------------------------
# ⚙️ Page Config
# -----------------------------
st.set_page_config(
    page_title="Tech Research Assistant",
    layout="wide"
)

# -----------------------------
# 🧠 Load Graph
# -----------------------------
@st.cache_resource
def load_graph():
    return build_graph()

graph = load_graph()

# -----------------------------
# 🧠 LLM-Based Query Classifier
# -----------------------------
def classify_query(query: str) -> str:
    response = llm.invoke(f"""
Classify the user query.

Query: {query}

Answer ONLY one word:
TECH or NON-TECH
""").content.strip().upper()

    return response


# -----------------------------
# 💬 Session State
# -----------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -----------------------------
# 🎨 Sidebar
# -----------------------------
with st.sidebar:
    st.title("⚙️ Controls")

    if st.button("🧹 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

    st.markdown("---")
    st.subheader("📊 System Info")
    st.write("Domain: Technology")
    st.write("Mode: LLM-controlled routing")

# -----------------------------
# 🏠 Main UI
# -----------------------------
st.title("💻 Tech Research Assistant")
st.caption("LangGraph + Groq + Tavily | Intelligent AI System")

# -----------------------------
# 💬 Chat History
# -----------------------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# -----------------------------
# 🧑 User Input
# -----------------------------
query = st.chat_input("Ask a technology question...")

if query:
    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": query
    })

    with st.chat_message("user"):
        st.markdown(query)

    # -----------------------------
    # 🧠 LLM Classification
    # -----------------------------
    with st.chat_message("assistant"):
        with st.spinner("🧠 Understanding query..."):

            label = classify_query(query)

    # -----------------------------
    # 🚫 NON-TECH → Reject
    # -----------------------------
    if label == "NON-TECH":

        response = """⚠️ I can only answer technology-related questions.

Try asking:
- What is LangGraph?
- React vs Angular
- How does Kubernetes work?
"""

        with st.chat_message("assistant"):
            st.markdown(response)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })

    # -----------------------------
    # ✅ TECH → Run Pipeline
    # -----------------------------
    else:
        with st.chat_message("assistant"):
            with st.spinner("🤖 Generating report..."):

                start = time.time()

                result = graph.invoke({
                    "query": query,
                    "research_data": [],
                    "analysis": "",
                    "report": "",
                    "sources": [],
                    "messages": [],
                    "steps_log": []
                })

                end = time.time()

                report = result.get("report", "No report generated.")
                sources = result.get("sources", [])
                steps = result.get("steps_log", [])
                latency = round(end - start, 2)

                # -----------------------------
                # 📄 Report
                # -----------------------------
                st.markdown("### 📄 Report")
                st.markdown(report)

                # -----------------------------
                # 🔗 Sources
                # -----------------------------
                if sources:
                    with st.expander("🔗 Sources"):
                        for s in sources:
                            title = s.get("title", "No Title")
                            url = s.get("url", "#")
                            st.markdown(f"- [{title}]({url})")

                # -----------------------------
                # 📊 Execution Logs
                # -----------------------------
                with st.expander("📊 Execution Details"):
                    st.write(f"⏱️ Latency: {latency}s")
                    st.write(f"🔁 Steps: {len(steps)}")
                    st.json(steps)

        # Save response
        st.session_state.messages.append({
            "role": "assistant",
            "content": report
        })