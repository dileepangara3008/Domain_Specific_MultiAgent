def supervisor_node(state):
    print("\n🧠 SUPERVISOR")

    if not state.get("research_data"):
        return {**state, "next_agent": "research"}

    if not state.get("analysis"):
        return {**state, "next_agent": "analysis"}

    if not state.get("report"):
        return {**state, "next_agent": "report"}

    return {**state, "next_agent": "end"}