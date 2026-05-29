from llm import llm

def analysis_agent(state):
    print("\n📊 ANALYSIS AGENT")

    formatted_data = "\n".join(
        f"{d['title']}: {d['content']}" for d in state["research_data"]
    )

    analysis = llm.invoke(f"""
        You are a technology expert.

        Analyze the following data with focus on:

        1. Core concept and explanation
        2. Real-world applications
        3. Latest trends and innovations
        4. Advantages and limitations
        5. Future scope and impact

        Data:
        {formatted_data}
    """).content

    state["steps_log"].append({
        "agent": "analysis",
        "domain": "technology",
        "status": "done"
    })

    return {
        **state,
        "analysis": analysis,
        "next_agent": "supervisor"
    }