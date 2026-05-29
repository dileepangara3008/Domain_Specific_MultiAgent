from tools import tavily_search

def research_agent(state):
    print("\n🔍 RESEARCH AGENT")

    try:
        query = state["query"]

        # 💻 Technology-focused query
        domain_query = f"Technology: {query} AI software development cloud computing data science trends"

        results = tavily_search(domain_query)

        print("DEBUG RESEARCH RESULTS:", results)

        state["steps_log"].append({
            "agent": "research",
            "domain": "technology",
            "status": "done"
        })

        return {
            **state,
            "research_data": results,
            "sources": results,
            "next_agent": "supervisor"
        }

    except Exception as e:
        return {
            **state,
            "research_data": [],
            "sources": [],
            "error": str(e),
            "next_agent": "supervisor"
        }