from langgraph.graph import StateGraph, END
from state import AgentState

from nodes.supervisor import supervisor_node
from nodes.research import research_agent
from nodes.analysis import analysis_agent
from nodes.report import report_agent


def router(state):
    if state.get("error"):
        return "end"
    return state["next_agent"]

def build_graph():
    builder = StateGraph(AgentState)

    builder.add_node("supervisor", supervisor_node)
    builder.add_node("research", research_agent)
    builder.add_node("analysis", analysis_agent)
    builder.add_node("report", report_agent)

    builder.set_entry_point("supervisor")

    builder.add_conditional_edges(
        "supervisor",
        router,
        {
            "research": "research",
            "analysis": "analysis",
            "report": "report",
            "end": END
        }
    )

    builder.add_edge("research", "supervisor")
    builder.add_edge("analysis", "supervisor")
    builder.add_edge("report", "supervisor")

    return builder.compile()