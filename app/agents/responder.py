from app.llm.litellm_client import (
    llm_call
)

from app.cache.semantic_cache import (
    get_cache,
    set_cache
)

from app.memory.vector_memory import (
    get_memory
)


async def response_agent(
        state
):

    query=state["query"]

    cached=get_cache(
        query
    )

    if cached:

        state["answer"]=cached

        return state

    memory=await get_memory(
        query
    )

    prompt=f"""

Question:

{query}

Context:

{state['context']}

Memory:

{memory}

Critic Notes:

{state['review']}

Generate answer.

"""

    response = await llm_call(prompt)

    state["answer"] = response["content"]
    state["token_count"] = response["token_count"]
    state["model"] = response["model"]

    set_cache(
        query,
        response
    )

    return state