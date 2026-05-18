from fastapi import (
    APIRouter
)

from pydantic import (
    BaseModel
)

from app.agents.workflow import (
    graph
)

router=APIRouter()


class AgentRequest(
        BaseModel
):

    session_id:str
    message:str


@router.post(
    "/agents/chat"
)
async def agent_chat(
        request:
        AgentRequest
):

    result=await graph.ainvoke(

        {
            "query":
            request.message,

            "session_id":
            request.session_id
        }

    )

    return {

        "response":
        result["answer"]
    }


@router.get(
    "/agents/workflow"
)
async def workflow_graph():

    return {

        "workflow":[

            "Planner",

            "Retriever",

            "Critic",

            "Responder"
        ]
    }