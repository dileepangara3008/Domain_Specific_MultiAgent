# 🚀 Tech Research Assistant (Streamlit + LangGraph + Groq)

An advanced **AI-powered multi-agent system** that generates detailed **technology-focused reports** using **LangGraph, Groq LLM, and Tavily search**, with a modern **ChatGPT-style Streamlit interface**.

---

## 📌 Overview

This project is an **interactive AI assistant** that:

* 💬 Accepts user queries via chat UI
* 🧠 Uses LLM to **classify queries (TECH / NON-TECH)**
* 🔍 Performs real-time **web research (Tavily)**
* 📊 Generates **deep analysis (LLM)**
* 📝 Produces **structured reports with sources**
* 🚫 Rejects non-technology queries intelligently

---

## 🧠 Architecture

```text
User Query
   ↓
🧠 LLM Classifier (TECH / NON-TECH)
   ↓
IF NON-TECH → Reject Response
IF TECH →
   ↓
🔍 Research Agent
   ↓
📊 Analysis Agent
   ↓
📝 Report Agent
   ↓
Final Report
```

---

## ⚙️ Tech Stack

* **Streamlit** – Web UI (chat interface)
* **LangGraph** – Multi-agent orchestration
* **LangChain** – LLM integration
* **Groq (LLaMA 3.1)** – Fast inference
* **Tavily API** – Web search
* **Python** – Core backend

---

## 📁 Project Structure

```text
.
├── app.py                  # Streamlit UI (main app)
├── graph.py                # LangGraph workflow
├── llm.py                  # Groq LLM config
├── state.py              
├── agents/
│   ├── research_agent.py
│   ├── analysis_agent.py
│   ├── report_agent.py
│   └── supervisor.py
├── tools.py  
├── .env
└── README.md
```

---

## 🔑 Setup Instructions

### 1. Clone repository

```bash
git clone <your-repo-url>
cd <repo-name>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add API keys

Create `.env` file:

```env
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 💻 Features

### 💬 Chat Interface

* ChatGPT-style UI
* Persistent chat history

### 🧠 Intelligent Query Handling

* LLM classifies query:

  * ✅ TECH → full pipeline
  * ❌ NON-TECH → polite rejection

### 📄 Structured Reports

* Executive summary
* Technical explanation
* Tools & technologies
* Use cases
* Trends & future scope
* Sources (no hallucinations)

### 📊 Observability

* Latency tracking
* Step logs
* Expandable debug info

---

## 🔍 Example Queries

### ✅ Valid (Technology)

* What is LangGraph?
* React vs Angular
* Explain vector databases
* How does Kubernetes work?

### ❌ Invalid (Rejected)

* Who is Virat Kohli
* Tell me a joke
* Hi / Hello

---

## 🚫 Non-Tech Handling

If user asks non-technology question:

```text
⚠️ I can only answer technology-related questions.

Try asking:
- What is LangGraph?
- React vs Angular
- How does Kubernetes work?
```

---

## 🔄 Workflow Logic

```python
if query == NON-TECH:
    return rejection_message
else:
    run LangGraph pipeline
```

---

## 🚀 Future Improvements

* [ ] Streaming responses (typing effect)
* [ ] Subdomain classification (AI / Web / Cloud)
* [ ] FastAPI backend
* [ ] User authentication
* [ ] Deployment (Streamlit Cloud)
* [ ] Memory (context-aware chat)

---

## 👨‍💻 Author

**Dileep Angara**

* B.Tech CSE @ RGUKT Nuzvid
* Focus: AI Systems, NLP, Multi-Agent Architectures

---

## 📜 License

MIT License

---

## ⭐ Acknowledgements

* LangChain & LangGraph
* Groq (LLaMA models)
* Tavily Search API

---

✨ *Built as a real-world AI system with controlled LLM behavior and multi-agent workflows.*
