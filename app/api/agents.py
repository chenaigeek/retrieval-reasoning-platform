from fastapi import APIRouter

from pydantic import BaseModel

from app.agents.workflow import graph
from app.monitoring.evaluator import hallucination_rate

router = APIRouter()


class AgentRequest(BaseModel):

    session_id: str
    message: str


@router.post("/agents/chat")
async def agent_chat(request: AgentRequest):

    result = await graph.ainvoke(
        {"query": request.message, "session_id": request.session_id}
    )

    score = hallucination_rate(result["answer"], result["context"])

    return {
        "response": result["answer"],
        "hallucination_rate": score,
        "model_used": result["model"],
    }


@router.get("/agents/workflow")
async def workflow_graph():

    return {"workflow": ["Planner", "Retriever", "Critic", "Responder"]}
