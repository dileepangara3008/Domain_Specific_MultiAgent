# 🚀 Tech Research Assistant (LangGraph + Groq + Tavily)

An advanced **AI-powered multi-agent system** that generates detailed **technology-focused reports** from user queries using **LangGraph, Groq LLM (LLaMA 3.1), and Tavily search**.

---

## 📌 Overview

This project is an **interactive CLI-based AI assistant** that:

* Accepts **technology-related queries**
* Performs **real-time web research**
* Generates **deep analysis using LLMs**
* Produces **structured reports with verified sources**
* Supports **multiple queries in a loop**

---

## 🧠 Architecture

```text
User Query
   ↓
🧠 Supervisor Agent (controls flow)
   ↓
🔍 Research Agent (Tavily Search)
   ↓
📊 Analysis Agent (LLM reasoning)
   ↓
📝 Report Agent (structured output)
   ↓
Final Report
```

---

## ⚙️ Tech Stack

* **LangGraph** – Multi-agent workflow orchestration
* **LangChain** – LLM integration
* **Groq (LLaMA 3.1)** – Fast inference engine
* **Tavily API** – Real-time web search
* **Python** – Core backend

---

## 📁 Project Structure

```text
.
├── main.py                  # CLI loop entry point
├── graph.py                 # LangGraph workflow builder
├── llm.py                   # Groq LLM configuration
├── agents/
│   ├── research_agent.py
│   ├── analysis_agent.py
│   ├── report_agent.py
│   └── supervisor.py
├── tools/
│   └── tavily_search.py
├── .env                     # API keys
└── README.md
```

---

## 🔑 Setup Instructions

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd <repo-name>
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key
```

---

## ▶️ Run the Application

```bash
python main.py
```

---

## 💻 Usage

```text
💻 Tech Research Assistant

👉 Enter your question: What is LangGraph?

✅ FINAL REPORT:
[Generated structured report]

------------------------------------------------------------

👉 Enter your question: React vs Angular

✅ FINAL REPORT:
[Comparison report]

------------------------------------------------------------

👉 Enter your question: Future of AI agents

✅ FINAL REPORT:
[Trend analysis]

------------------------------------------------------------

👉 exit
👋 Goodbye!
```

---

## 🔍 Agents Explained

### 🧠 Supervisor Agent

* Controls workflow execution
* Routes between agents based on state

---

### 🔍 Research Agent

* Uses Tavily API
* Fetches real-time technology-related data

---

### 📊 Analysis Agent

* Processes research data
* Extracts insights using LLM reasoning

---

### 📝 Report Agent

* Generates structured reports
* Adapts format based on user query
* Ensures **no hallucinated sources**

---

## 🔄 Workflow Logic

```python
if not research_data:
    → research_agent
elif not analysis:
    → analysis_agent
elif not report:
    → report_agent
else:
    → end
```

---

## 📊 Features

* ✅ Multi-agent architecture (LangGraph)
* ✅ Technology-only domain specialization
* ✅ Dynamic report generation (query-aware)
* ✅ Source-backed outputs (no fake links)
* ✅ Interactive CLI (multi-query loop)
* ✅ Graph visualization (Mermaid PNG)
* ✅ Logging + latency tracking

---

## ⚠️ Limitations

* Limited to **technology domain**
* Dependent on external APIs (Groq, Tavily)
* No persistent memory (stateless queries)

---

## 🚀 Future Improvements

* [ ] Streamlit / Web UI
* [ ] FastAPI backend
* [ ] Streaming responses
* [ ] Subdomain classification (AI, Web, Cloud)
* [ ] Memory (context-aware queries)
* [ ] JSON structured outputs
* [ ] LangSmith tracing & evaluation

---

## 🧪 Example Queries

* What is LangGraph?
* React vs Angular
* Explain vector databases
* Future of AI agents
* How does Kubernetes work?

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

✨ *Built to explore real-world AI system design using multi-agent workflows.*
