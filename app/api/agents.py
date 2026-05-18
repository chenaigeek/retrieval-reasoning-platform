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
            request.message
        }

    )

    return {

        "response":
        result["answer"],

        "plan":
        result["plan"],

        "critic":
        result["review"]
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