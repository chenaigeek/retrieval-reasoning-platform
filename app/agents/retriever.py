from app.retrieval.rag import (
    retrieve_context
)


async def retriever_agent(
        state
):

    context=await retrieve_context(

        state["query"]

    )

    state["context"]=context

    return state