from typing import TypedDict

from langgraph.graph import StateGraph, END

from app.agents.planner import planner_agent

from app.agents.retriever import retriever_agent

from app.agents.critic import critic_agent

from app.agents.responder import response_agent


class AgentState(TypedDict):
    query: str
    plan: str
    context: str
    review: str
    answer: str
    token_count: int
    model: str


workflow = StateGraph(AgentState)

workflow.add_node("planner", planner_agent)

workflow.add_node("retriever", retriever_agent)

workflow.add_node("critic", critic_agent)

workflow.add_node("responder", response_agent)


workflow.set_entry_point("planner")

workflow.add_edge("planner", "retriever")

workflow.add_edge("retriever", "critic")

workflow.add_edge("critic", "responder")

workflow.add_edge("responder", END)


graph = workflow.compile()
