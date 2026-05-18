from app.llm.litellm_client import (
    llm_call
)


async def response_agent(
        state
):

    prompt=f"""

Question:

{state['query']}

Plan:

{state['plan']}

Retrieved Context:

{state['context']}

Critic Notes:

{state['review']}

Generate final answer.

"""

    answer=await llm_call(
        prompt
    )

    state["answer"]=answer

    return state