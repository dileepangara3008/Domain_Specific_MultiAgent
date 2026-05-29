from typing import TypedDict, List

class AgentState(TypedDict):
    query: str
    research_data: list   
    analysis: str
    report: str
    sources: list        
    next_agent: str
    messages: list
    steps_log: list 