from llm import llm

def report_agent(state):
    print("\n📝 REPORT AGENT")

    query = state.get("query", "")

    sources_text = "\n".join(
        f"{s.get('title','No Title')} ({s.get('url','')})"
        for s in state.get("sources", [])
    )

    report = llm.invoke(f"""
You are a senior technology expert and report writer.

Your task is to generate a detailed report ONLY in the TECHNOLOGY domain.

STRICT RULES:
- Focus strictly on technology-related interpretation
- Adapt structure based on the user query
- Use ONLY the provided data
- Do NOT invent sources

USER QUERY:
{query}

GUIDELINES:
- Identify what area of technology the query belongs to (AI, Web, Cloud, Data Science, etc.)
- Create relevant sections dynamically (not fixed)
- Keep explanations clear and insightful
- Include real-world relevance wherever possible

MANDATORY SECTIONS:
1. Executive Summary
2. Detailed Analysis (dynamic sections based on query)
3. Key Insights / Takeaways
4. Sources with URLs

Research Data:
{state.get('research_data', [])}

Analysis:
{state.get('analysis', '')}

Sources:
{sources_text}
""").content

    state["steps_log"].append({
        "agent": "report",
        "domain": "technology",
        "status": "done"
    })

    return {
        **state,
        "report": report,
        "next_agent": "supervisor"
    }